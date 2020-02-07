import json
import json
import logging
import time
from automation_framework.utilities.workflow import submit_request
from automation_framework.work_order_receipt.wo_receipt_params \
    import WorkOrderReceipt
from automation_framework.work_order_submit.work_order_submit_params \
    import WorkOrderSubmit
from automation_framework.utilities.request_args import GetResultWaitTime
logger = logging.getLogger(__name__)


def submit_work_order(input_request, input_type, tamper,
                      output_json_file_name,
                      uri_client, worker_obj,
                      request_method,
                      private_key, err_cd):
    """ Function to submit work order receipt create
        Read input request from string or
         object and submit request.
        Uses WorkOrderReceiptCreate class definition
         to create receipt object.
        Triggers submit requestt, validate_response_code,
        Returns - error code, input_json_str1,
         response, processing_time,
        worker_obj, sig_obj, encrypted_session_key. """

    response = {}

    if err_cd == 0:
        # --------------------------------------------------------------------
        logger.info("------ Testing WorkOrderSubmit API ------")

        if input_type == "object":
            input_work_order = json.loads(input_request.to_string())
        else:
            wo_submit_request = {
                "jsonrpc": "2.0",
                "method": "WorkOrderSubmit",
                "id": 11,
                "params": {
                    "responseTimeoutMSecs": 6000,
                    "payloadFormat": "JSON-RPC",
                    "resultUri": "resulturi",
                    "notifyUri": "notifyuri",
                    "workOrderId": "",
                    "workerId": "",
                    "workloadId": "heart-disease-eval",
                    "requesterId": "0x3456",
                    "workerEncryptionKey": "",
                    "dataEncryptionAlgorithm": "AES-GCM-256",
                    "encryptedSessionKey": "",
                    "sessionKeyIv": "",
                    "requesterNonce": "",
                    "encryptedRequestHash": "",
                    "requesterSignature": "",
                    "inData": [
                        {"index": 0,
                         "data": "Heart disease evaluation data: 32 \
                                 1 1 156  132 125 1 95  1 0 1 1 3 1"
                         }
                    ]
                }
            }

        wo_obj_submit = WorkOrderSubmit()
        wo_obj = WorkOrderReceipt()
        wo_obj_submit.add_json_values(wo_submit_request,
                                      worker_obj, private_key,
                                      tamper)
        input_work_order_submit = wo_obj_submit.compute_signature(tamper)

        input_json_str1 = json.loads(input_work_order_submit)
        response = submit_request(uri_client, input_json_str1,
                                  output_json_file_name)

        # create work order receipt request
        # wo_obj = WorkOrderReceipt()
        input_work_order = wo_obj.add_json_values(input_request, worker_obj,
                                                  private_key,
                                                  tamper,
                                                  input_work_order_submit)
        input_work_order = wo_obj.compute_signature(tamper)
        logger.info('''Compute Signature complete \n''')

        # logger.info('''Request to be submitted
        # for receipt: %s \n''', input_work_order)
        input_json_str1 = json.loads(input_work_order)
        response = submit_request(uri_client, input_json_str1,
                                  output_json_file_name)
        time.sleep(GetResultWaitTime.LOOP_WAIT_TIME.value)
        # err_cd = validate_response_code(response, check_submit)

        work_order_id = wo_obj.get_work_order_id()
    else:
        logger.info('''ERROR: No Worker Retrieved from system.
                   Unable to proceed to process work order.''')
    return response
