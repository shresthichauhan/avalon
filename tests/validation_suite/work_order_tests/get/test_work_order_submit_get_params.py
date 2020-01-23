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

import pytest
import logging
import json
from work_order_tests.work_order_tests import work_order_get_result_params, \
    work_order_request_params
from automation_framework.work_order_submit.work_order_submit_utility \
    import verify_work_order_signature, decrypt_work_order_response
from automation_framework.utilities.request_args import TestStep
from automation_framework.utilities.workflow import validate_response_code

logger = logging.getLogger(__name__)


def test_work_order_submit_requesterNonce_all_special_characters(setup_config):
    """ Testing work order request by submiting
    requesterNonce with special characters. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_submit_requesterNonce_all_special_characters.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
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


def test_work_order_workerEncryptionKey_special_character(setup_config):
    """ Testing work order request by submiting
    worker encryption key with special characters. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_workerEncryptionKey_special_character.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
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


def test_work_order_with_alternate_worker_signing_algorithm(setup_config):
    """ Testing work order request
    by submiting alternate signing algorithm. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_with_alternate_worker_signing_algorithm.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
                                               generic_params))

    setup_config[0].signingAlgorithm = "RSA-OAEP-3072"

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


def test_work_order_with_alternate_hashing_algorithm(setup_config):
    """ Testing work order request by
    submiting alternate hashing algorithm. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_with_alternate_hashing_algorithm.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
                                               generic_params))

    setup_config[0].hashingAlgorithm = "SHA-512"

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


def test_work_order_without_requester_private_key(setup_config):
    """ Testing work order request by
    submiting without requester private key. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_without_requester_private_key.json'
    private_key = ""

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
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


def test_work_order_submit_twice_params(setup_config):
    """ Testing work order request by passing the
    parameters twice in the request. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_submit_twice_params.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
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


def test_work_order_invalid_parameter(setup_config):
    """ Testing work order request by passing wrong workloadid. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_invalid_parameter.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
                                               generic_params))

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_signature_with_wrong_payload_format(setup_config):
    """ Testing work order request by passing wrong payload format. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_signature_with_wrong_payload_format.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
                                               generic_params))

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_submit_requesterId_param_remove(setup_config):
    """ Testing work order request without requesterId. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_submit_requesterId_param_remove.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
                                               generic_params))

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_submit_workload_id_hex_string(setup_config):
    """ Testing work order request valid hex string workloadid. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_submit_workload_id_hex_string.json'
    tamper = {"params": {"before_sign": {"workloadId": ""}}}

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
                                               generic_params))

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_submit_workload_id_random_string(setup_config):
    """ Test work order request with wrong workload id """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_submit_workload_id_random_string.json'
    tamper = {"params": {"before_sign": {"workloadId": ""}}}

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
                                               generic_params))

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_workloadId_specialcharacters(setup_config):
    """ Test work order request with wrong workload id """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_workloadId_specialcharacters.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
                                               generic_params))

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_with_not_supported_dataencryption_algorithm(setup_config):
    """ Test work order request with  unsupported dataencryption algorithm  """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_with_not_supported_dataEncryption_algorithm.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
                                               generic_params))

    # WorkOrderGetResult API Response validation with key parameters
    assert (validate_response_code(work_order_get_result_response) is
            TestStep.SUCCESS.value)


def test_work_order_with_wrong_worker_signing_algorithm(setup_config):
    """ Testing work order request with wrong signing algorithm. """

    # input file name
    request = 'work_order_tests/input' \
              '/work_order_with_wrong_worker_signing_algorithm.json'

    work_order_response, generic_params = (work_order_request_params
                                           (setup_config, request))
    err_cd, work_order_get_result_response = (work_order_get_result_params
                                              (work_order_response[:6],
                                               generic_params))

    setup_config[0].signingAlgorithm = "SECP128K1"

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
