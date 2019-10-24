import pytest
import logging
import json
import worker_utility

logger = logging.getLogger(__name__)

def test_worker_lookup_workerType_not_unsigned_int(setup_config):
    """ Testing worker lookup for invalid worker type by using not unsigned integer.
        Validate the response with totalcount result field """
    # retrieve values from conftest session fixture
    worker_obj = setup_config[0]
    sig_obj = setup_config[1]
    uri_client = setup_config[2]
    private_key = setup_config[3]
    err_cd = setup_config[4]

    # input and output names
    input_json_file = r'./worker/input/worker_lookup_workerType_not_unsigned_int.json'
    id_gen = False
    output_json_file_name = 'worker_lookup_workerType_not_unsigned_int'

    # expected response
    check_worker_result = {"result": {"totalCount": 0}}

    err_cd, worker_obj, input_json_str1, response = worker_utility.process_worker_actions(input_json_file, id_gen, output_json_file_name, worker_obj, uri_client, check_worker_result)

    if response["result"]["totalCount"] == 0:
        err_cd = 0
    else:
        err_cd = 1

    assert err_cd == 0


def test_worker_lookup_empty_params(setup_config):
    """Testing worker lookup with empty parameter and validate the  response """
    # retrieve values from conftest session fixture
    worker_obj = setup_config[0]
    sig_obj = setup_config[1]
    uri_client = setup_config[2]
    private_key = setup_config[3]
    err_cd = setup_config[4]

    # input and output names
    input_json_file = r'./worker/input/worker_lookup_empty_params.json'
    id_gen = False
    output_json_file_name = 'worker_lookup_empty_params'

    # expected response
    check_worker_result = {"result": {"totalCount": 1}}

    err_cd, worker_obj, input_json_str1, response = worker_utility.process_worker_actions(input_json_file, id_gen, output_json_file_name, worker_obj, uri_client, check_worker_result)

    if response["result"]["totalCount"] > 0:
        err_cd = 0
    else:
        err_cd = 1

    assert err_cd == 0


def test_worker_lookup_method_field_change(setup_config):
    """Testing the worker lookup request by changing method field of API.
        Validate the response """
    # retrieve values from conftest session fixture
    worker_obj = setup_config[0]
    sig_obj = setup_config[1]
    uri_client = setup_config[2]
    private_key = setup_config[3]
    err_cd = setup_config[4]

    # input and output names
    input_json_file = r'./worker/input/worker_lookup_method_field_change.json'
    id_gen = False
    output_json_file_name = 'worker_lookup_method_field_change'

    # expected response
    check_worker_result = {"error": {"code": -32601}}
    check_worker_result = {"error": {"message": "Method not found"}}

    err_cd, worker_obj, input_json_str1, response = worker_utility.process_worker_actions(input_json_file, id_gen, output_json_file_name, worker_obj, uri_client, check_worker_result)

    assert err_cd == 0    


def test_worker_lookup_jsonrpc_different_version(setup_config):
    """Testing the worker lookup request by modifying jsonrpc version.
       Velidation the response """
    # retrieve values from conftest session fixture
    worker_obj = setup_config[0]
    sig_obj = setup_config[1]
    uri_client = setup_config[2]
    private_key = setup_config[3]
    err_cd = setup_config[4]

    # input and output names
    input_json_file = r'./worker/input/worker_lookup_jsonrpc_different_version.json'
    id_gen = False
    output_json_file_name = 'worker_lookup_jsonrpc_different_version'

    # expected response
    check_worker_result = {"result": {"totalCount": 1}}

    err_cd, worker_obj, input_json_str1, response = worker_utility.process_worker_actions(input_json_file, id_gen, output_json_file_name, worker_obj, uri_client, check_worker_result)
    
    if response["result"]["totalCount"] > 0:
        err_cd = 0
    else:
        err_cd = 1

    assert err_cd == 0
