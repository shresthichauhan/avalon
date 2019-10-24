import pytest
import logging
import json
import random
import utility.file_utils as futils
import work_order_utility

logger = logging.getLogger(__name__)

@pytest.mark.run('second-to-last')
def test_work_order_with_same_workerid_workerorderid(setup_config):
    """ Testing work order request with all valid parameter values. """

    # retrieve values from conftest session fixture
    worker_obj = setup_config[0]
    sig_obj = setup_config[1]
    uri_client = setup_config[2]
    private_key = setup_config[3]
    err_cd = setup_config[4]

    # input and output names
    input_json_01 = './work_order/input/work_order_with_same_workerid_workerorderid.json'
    input_type = 'string'
    output_json_file_name = 'work_order_with_same_workerid_workerorderid'
    tamper = {"params": {}}

    logger.info("------------------Input file name: %s ---------------\n", input_json_01)
    input_json_str1 = futils.read_json_file(input_json_01)
    # reuse workorder id and incrment reuest id
    input_json_temp = json.loads(input_json_str1)
    input_json_temp["params"]["workOrderId"] = worker_obj.worker_id
    input_json_temp["params"]["workerId"] = worker_obj.worker_id
    input_json_str2 = json.dumps(input_json_temp)

    # expected response
    check_submit = {"error": {"code": 5}}
    check_result = '''{"result": {"workOrderId": "", "workloadId": "",
                   "workerId": "", "requesterId": "", "workerNonce": "",
                   "workerSignature": "", "outData": ""}}'''
    check_get_result = json.loads(check_result)

    # process worker actions
    (err_cd, input_json_str1, response_01, processing_time,
    worker_obj, sig_obj, session_key, session_iv,
    enc_session_key) = work_order_utility.process_work_order(input_json_str2,
    input_type, tamper, output_json_file_name, worker_obj, sig_obj,
    uri_client, private_key, err_cd, check_submit, check_get_result)
    
    if err_cd == 0:
        err_cd = work_order_utility.verify_work_order_signature(response_01,
                                             sig_obj, worker_obj)

    if err_cd == 0:
        (err_cd, decrypted_data) = (work_order_utility.
                decrypt_work_order_response(response_01, session_key, session_iv))

    if err_cd == 0:
        logger.info('''Test Case Success : Work Order Processed successfully
                    with Signature Verification and Decrypted Response \n''')
    else:
        logger.info('''Test Case Failed : Work Order Not Processed successfully
                    with Signature Verification and Decrypted Response''')

    assert err_cd == 0
