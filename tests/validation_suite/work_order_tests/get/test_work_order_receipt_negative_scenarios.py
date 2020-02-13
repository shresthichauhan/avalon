# Copyright 2019 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import json
import utility.file_utils as futils

from automation_framework.utilities.post_request import \
    post_request
from automation_framework.utilities.request_args import TestStep
from automation_framework.utilities.workflow import validate_response_code

logger = logging.getLogger(__name__)


def test_work_order_receipt_create_requester_signature_not_match(setup_config):
    """ Testing work order receipt create requester signature
    does not match. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_tests/input/' \
                      'work_order_receipt_wrong_requester_signature.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}
    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)


def test_work_order_receipt_workorder_id_not_match(setup_config):
    """ Testing work order request with all valid parameter values. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]
    # input file name
    input_json_file = 'work_order_tests/input/work_order_receipt.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}
    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)


def test_create_work_order_receipt_with_wrong_signature_rules(setup_config):
    """ Testing work order receipt
     with wrong signature rules. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_tests/input' \
                      '/work_order_receipt_signature.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}
    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)


def test_create_work_order_receipt_with_same_requester_id(setup_config):
    """ Testing work order receipt with same requester id. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_tests/input' \
                      '/work_order_receipt_with_same_requester_id.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}
    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)


def test_create_work_order_receipt_with_empty_workerserviceid(setup_config):
    """ Testing work order request with empty service id. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_tests/input' \
                      '/work_order_receipt_with_empty_workerserviceid.json'
    # input type - file, string or object

    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {"workerServiceId": ""}}
    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)


def test_create_work_order_receipt_with_empty_workerid(setup_config):
    """ Testing work order request with
     all valid parameter values. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input file name
    input_json_file = 'work_order_tests/input' \
                      '/work_order_receipt_with_empty_workerid.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {"workerId": ""}}
    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)


def test_create_work_order_receipt_with_empty_Requesthash(setup_config):
    """ Testing work order request
     with empty Requesthash. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_tests/input' \
                      '/work_order_receipt_with_empty_Requesthash.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}
    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)


'''def test_create_work_order_receipt_without_sign_rule_param(setup_config):
    """ Testing work order receipt
     with random hex string without signature rules param. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input file name
    input_json_file = 'work_order_receipt/' \
                      'input/work_order_receipt_without_signature_rule.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}

    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)


def test_create_work_order_receipt_without_requesterSignature(setup_config):
    """ Testing work order receipt with
     random hex strin in workorderRequestHash. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_receipt/input' \
                      '/work_order_receipt_without_requestersignature.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}

    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)'''


def test_create_work_order_receipt_invalid_requester_id(setup_config):
    """ Testing work order receipt with invalid reuqester id. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_tests/input/' \
                      'work_order_receipt_invalid_requester_id.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}
    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)


def test_create_work_order_receipt_hexstr_workorderRequesthash(setup_config):
    """ Testing work order receipt with
    random hex strin in workorderRequestHash. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_tests/input/' \
                      'work_order_receipt_hexstr_workorderRequesthash.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}

    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)


def test_create_work_order_receipt_wrong_rverificationkey(setup_config):
    """ Testing work order receipt with
    random hex string with wrong receipt verification. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_tests/input/' \
                      'work_order_receipt_wrong_rverificationkey.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}

    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)


def test_create_work_order_receipt_diff_hex_str_rg_rs(setup_config):
    """ Testing work order receipt with
    random hex strin in requesternounce and signature. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_tests/input/' \
                      'work_order_receipt_diff_hex_str_rG_rs.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}

    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)


'''def test_create_work_order_same_workerSerive_workorderid(setup_config):
    """ Testing work order receipt with
    random hex strin in requesternounce and signature. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_receipt/input/' \
                      'work_order_receipt_same_ws_wo.json'
    # input type - file, string or object


    input_type = ''
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}

    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"
        # read json input file for the test case
   # input_json_temp = input_json_file
   # logger.info("------ Loaded string data: %s ------\n", input_json_file)

    #input_json_temp = input_json
   # input_json_temp["params"]["workOrderId"] = worker_obj.worker_id
   # input_json_temp["params"]["workerServiceId"] = worker_obj.worker_id
   # input_json_file = json.dumps(input_json_temp)
  #  logger.info("\n 1111111%s \n\n", input_json_file)

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)

    response_tup = post_request(request_tup)
    input_type = 'string'
    input_request = 'string'
    request_mode = "string"
    tamper = {"params": {"workerServiceId": ""}}


    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    logger.info("\n 1111111%s \n\n", request_tup)

    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)


def test_create_work_order_receipt_twice(setup_config):
    """ Testing work order receipt with
    random hex strin in requesternounce and signature. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_receipt/input/' \
                      'work_order_receipt_with_random_workorderid.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}

    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    request_tup_1 = (input_json_file, input_type, tamper,
    output_json_file_name,uri_client,
     request_method, worker_obj, private_key, err_cd)

    response_tup = post_request(request_tup_1)

    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)'''


def test_create_work_order_receipt_default_value_rs(setup_config):
    """ Testing work order receipt with
    valid hex in requester signature. """

    # retrieve values from conftest session fixture
    worker_obj, uri_client, private_key, err_cd = setup_config[:4]

    # input parameter for processing work order receipt
    # input file name
    input_json_file = 'work_order_tests/input/' \
                      'work_order_receipt_default_value_rs.json'
    # input type - file, string or object
    input_type = 'file'
    # output filename
    output_json_file_name = 'work_order_receipt'
    # tamper parameters
    tamper = {"params": {}}

    # request method to be used when processing object input type
    request_method = "WorkOrderReceiptCreate"

    request_tup = (input_json_file, input_type, tamper, output_json_file_name,
                   uri_client, request_method, worker_obj, private_key, err_cd)
    response_tup = post_request(request_tup)
    assert (validate_response_code(response_tup) is TestStep.SUCCESS.value)
