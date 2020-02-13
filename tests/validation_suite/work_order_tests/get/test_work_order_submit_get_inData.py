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

from automation_framework.utilities.request_args import TestStep
from automation_framework.utilities.workflow import validate_response_code
from automation_framework.work_order_submit.work_order_submit_utility \
    import verify_work_order_signature, decrypt_work_order_response, \
    check_for_error_code
from work_order_tests.work_order_tests import work_order_get_result_params, \
    work_order_request_params

logger = logging.getLogger(__name__)


def test_work_order_DataEncryptionKey_hyphen_echo(setup_config):
    """ Testing work order request by passing hyphen key as clear text \
    for encrypteddataencryption in indata for echo client workload."""

    # input file name
    request = 'work_order_tests/' \
              'input/work_order_DataEncryptionKey_hyphen_echo.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (check_for_error_code(err_cd) is TestStep.SUCCESS.value)


def test_work_order_data_datahash_null(setup_config):
    """ Testing work order request with data and datahash null. """

    # input file name
    request = 'work_order_tests/input/work_order_data_datahash_null.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_datahash_random_str(setup_config):
    """ Testing work order request by passing random string in datahash"""

    # input file name
    request = 'work_order_tests/input/work_order_datahash_random_str.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_indata_index1_data_different_hexlength(setup_config):
    """Testing work order request with indata
    index1 data with different hex length."""

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_indata_index1_data_diff_len.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_submit_requesterId_null(setup_config):
    """ Testing work order request for setting requesterId as null. """

    # input file name
    request = 'work_order_tests/input/work_order_requester_id_null.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_iv_indata_hex_string(setup_config):
    """ Testing work order request by setting iv of indata to hex string. """
    # input file name
    request = 'work_order_tests/input/work_order_iv_indata_hex_string.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_indata_index1_data_special_char(setup_config):
    """Testing work order request with all
    special characters in index of indata """
    # input file name
    request = 'work_order_tests/input' \
              '/work_order_indata_index1_data_special_char.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_with_changing_order_index(setup_config):
    """Testing work order request with changing order index """
    # input file name
    request = 'work_order_tests/input' \
              '/work_order_with_changing_order_index.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_unknown_parameter(setup_config):
    """Testing work order request with unknown parameter in indata"""
    # input file name
    request = 'work_order_tests/input/work_order_unknown_parameter.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_with_empty_indata_hash(setup_config):
    """Testing work order request with empty indata hash"""
    # input file name
    request = 'work_order_tests/input/work_order_with_empty_indata_hash.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_with_index0_indata(setup_config):
    """Testing work order request with index 0"""

    # input file name
    request = 'work_order_tests/input/work_order_with_index0_indata.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_encryptedDataEncryptionKey_null(setup_config):
    """Testing work order by passing
    encryptedDataEncryptionKey null in index of indata."""

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_encryptedDataEncryptionKey_null.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_indata_outdata(setup_config):
    """Testing work order request with both indata and outdata ."""

    # input file name
    request = 'work_order_tests/input/work_order_indata_outdata.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_negative_index(setup_config):
    """Testing work order by passing negative index in indata."""

    # input file name
    request = 'work_order_tests/input/work_order_negative_index.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_with_50_index_indata(setup_config):
    """Testing work order by passing 50 index in indata."""

    # input file name
    request = 'work_order_tests/input/work_order_with_50_index_indata.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_dataEncryption_algorithm_invalid(setup_config):
    """testing work order request by
    passing invalid dataEncryption algorithm ."""

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_dataEncryption_algorithm_invalid.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_with_empty_data(setup_config):
    """Testing work order with empty data and data hash"""

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_with_empty_data_indata.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_submit_datahash_calculation(setup_config):
    """ Testing work order request by passing
    required parameters for dataHash calculation. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_submit_datahash_calculation.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_multiple_data_echoresult(setup_config):
    """ Testing work order request with multiple data
    in indata using eco-result has workloadid. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_multiple_data_echoresult.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_diff_text_data_indata_echoClient(setup_config):
    """ Testing work order request with different text data in
     indata using echo-result has workloadid. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_diff_text_data_indata_echoClient.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_with_no_indata(setup_config):
    """ Testing work order request with no indata """

    # input file name
    request = 'work_order_tests/input/work_order_with_no_indata.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:2],
                                               generic_params))

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)


def test_work_order_encryptedDataEncryptionKey_hyphen(setup_config):
    """ Testing work order by passing
     encryptedDataEncryptionKey hyphen in index of indata. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_encryptedDataEncryptionKey_hyphen.json'

    work_order_response, generic_params = work_order_request_params(
        setup_config, request)

    err_cd, work_order_get_result_response = work_order_get_result_params(
        work_order_response[:2], generic_params)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)

    logger.info('\t\t!!! Test completed !!!\n\n')


def test_work_order_with_indata_unknown_parameter_value(setup_config):
    """ Testing work order request by passing
     invalid indata. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_with_indata_unknown_parameter_value.json'

    work_order_response, generic_params = work_order_request_params(
        setup_config, request)

    err_cd, work_order_get_result_response = work_order_get_result_params(
        work_order_response[:2], generic_params)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)
    logger.info('\t\t!!! Test completed !!!\n\n')


def test_work_order_params_indata_first(setup_config):
    """ Testing work order request with indata first then params. """

    # input file name
    request = 'work_order_tests/input/work_order_params_indata_first.json'

    work_order_response, generic_params = work_order_request_params(
        setup_config, request)

    err_cd, work_order_get_result_response = work_order_get_result_params(
        work_order_response[:2], generic_params)

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)

    logger.info('\t\t!!! Test completed !!!\n\n')


def test_work_order_random_str_iv_echoresult(setup_config):
    """ Testing work order request by passing
     random string in iv. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_random_str_iv_echoresult.json'

    work_order_response, generic_params = work_order_request_params(
        setup_config, request)

    err_cd, work_order_get_result_response = work_order_get_result_params(
        work_order_response[:2], generic_params)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)
    logger.info('\t\t!!! Test completed !!!\n\n')


def test_work_order_submit_verifyingkey_null_str(setup_config):
    """ Testing work order request by passing verifyingkey null. """

    # input file name
    request = 'work_order_tests/input/' \
              'work_order_submit_verifyingkey_null_str.json'

    work_order_response, generic_params = work_order_request_params(
        setup_config, request)

    err_cd, work_order_get_result_response = work_order_get_result_params(
        work_order_response[:2], generic_params)

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)

    logger.info('\t\t!!! Test completed !!!\n\n')


def test_work_order_diff_text_data_indata(setup_config):
    """ Testing work order request by passing different
    text in indata(heart-disease-eval)
       Changed in input response :
       "data": "Heart disease evaluation data:
       25 10 1 67  102 125 1 95 5 10 1 11 36 1 1 2 3 5 9 7"
       Decryption message: Decryption result at client
       - Error with missing or incorrect input format. """

    # input file name
    request = 'work_order_tests/input/work_order_diff_text_data_indata.json'

    work_order_response, generic_params = work_order_request_params(
        setup_config, request)

    err_cd, work_order_get_result_response = work_order_get_result_params(
        work_order_response[:2], generic_params)

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)

    logger.info('\t\t!!! Test completed !!!\n\n')


def test_work_order_specialcharacter_index_indata(setup_config):
    """ Testing work order request by passing special characters
     in data field of indata.
        Change in input request : "data": "@!#$%"
        Decrypted message :Decryption result at client
         - Heart disease risk is 59% for 429 people"""

    # input file name
    request = 'work_order_tests/input/' \
              'work_order_specialcharacter_index_indata.json'

    work_order_response, generic_params = work_order_request_params(
        setup_config, request)

    err_cd, work_order_get_result_response = work_order_get_result_params(
        work_order_response[:2], generic_params)

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)

    logger.info('\t\t!!! Test completed !!!\n\n')


def test_work_order_specialcharacter_indata(setup_config):
    """ Testing work order request by passing special
     characters in data field of indata.
        Change in input request :
        "data": "Heart disease evaluation data:@#$!%"
        Decrypted message :
        Error with missing or incorrect input format"""

    # input file name
    request = 'work_order_tests/input/work_order_specialcharacter_indata.json'

    work_order_response, generic_params = work_order_request_params(
        setup_config, request)

    err_cd, work_order_get_result_response = work_order_get_result_params(
        work_order_response[:2], generic_params)

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)

    logger.info('\t\t!!! Test completed !!!\n\n')


def test_work_order_diff_data_indata(setup_config):
    """ Testing work order request by passing
     different text in indata(heart-disease-eval)
        Changes in input request:"data":
         "25 10 1 67  102 125 1 95 5 10 1 11 36 1 1 2 3 5 9 7"
       Decryption message:Decryption result at client
        - Heart disease risk is 59% for 431 people. """

    # input file name
    request = 'work_order_tests/input/work_order_diff_data_indata.json'

    work_order_response, generic_params = work_order_request_params(
        setup_config, request)

    err_cd, work_order_get_result_response = work_order_get_result_params(
        work_order_response[:2], generic_params)

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)

    logger.info('\t\t!!! Test completed !!!\n\n')


def test_work_order_alternate_DEA_echo(setup_config):
    """ Testing work order request by passing alternate data encryption
        algorithm (echo-client). """

    # input file name
    request = 'work_order_tests/input/work_order_alternate_DEA_echo.json'

    work_order_response, generic_params = work_order_request_params(
        setup_config, request)

    err_cd, work_order_get_result_response = work_order_get_result_params(
        work_order_response[:2], generic_params)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)

    logger.info('\t\t!!! Test completed !!!\n\n')


def test_work_order_response_timeout_str_special_char_echo(setup_config):
    """ Testing work order request by passing special characters
    in response time (echo-client). """

    # input file name
    request = 'work_order_tests/input/' \
              'work_order_response_timeout_str_special_char_echo.json'

    work_order_response, generic_params = work_order_request_params(
        setup_config, request)

    err_cd, work_order_get_result_response = work_order_get_result_params(
        work_order_response[:2], generic_params)

    assert (verify_work_order_signature(work_order_get_result_response,
                                        generic_params[0])
            is TestStep.SUCCESS.value)

    assert (decrypt_work_order_response(work_order_get_result_response,
                                        work_order_response[3],
                                        work_order_response[4])[0]
            is TestStep.SUCCESS.value)

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)

    logger.info('\t\t!!! Test completed !!!\n\n')
