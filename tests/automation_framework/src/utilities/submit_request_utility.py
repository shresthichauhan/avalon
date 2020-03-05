import logging
import json
import time
import os
import sys
from src.libs import constants
import config.config as pconfig
import globals
from avalon_sdk.direct.jrpc.jrpc_worker_registry import \
    JRPCWorkerRegistryImpl
from avalon_sdk.direct.jrpc.jrpc_work_order import \
    JRPCWorkOrderImpl
from avalon_sdk.worker.worker_details import WorkerType
from avalon_sdk.direct.jrpc.jrpc_work_order_receipt \
     import JRPCWorkOrderReceiptImpl
#from avalon_sdk.fabric.fabric_worker_registry \
#    import FabricWorkerRegistryImpl
#from avalon_sdk.fabric.fabric_work_order \
#    import FabricWorkOrderImpl
from avalon_sdk.ethereum.ethereum_worker_registry \
    import EthereumWorkerRegistryImpl
from avalon_sdk.ethereum.ethereum_work_order \
    import EthereumWorkOrderProxyImpl
logger = logging.getLogger(__name__)
TCFHOME = os.environ.get("TCF_HOME", "../../")


def _create_worker_registry_instance(blockchain_type, config):
    # create worker registry instance for direct/proxy model
    if blockchain_type == 'fabric':
        return FabricWorkerRegistryImpl(config)
    elif blockchain_type == 'ethereum':
        return EthereumWorkerRegistryImpl(config)
    else:
        return JRPCWorkerRegistryImpl(config)


def _create_work_order_instance(blockchain_type, config):
    # create work order instance for direct/proxy model
    if blockchain_type == 'fabric':
        return FabricWorkOrderImpl(config)
    elif blockchain_type == 'ethereum':
        return EthereumWorkOrderProxyImpl(config)
    else:
        return JRPCWorkOrderImpl(config)


def _create_work_order_receipt_instance(blockchain_type, config):
    # create work order receipt instance for direct/proxy model
    if blockchain_type == 'fabric':
        return None
    elif blockchain_type == 'ethereum':
        # TODO need to implement
        return None
    else:
        return JRPCWorkOrderReceiptImpl(config)


def submit_request_listener(
        uri_client, input_json_str1, output_json_file_name):
    logger.info("Listener code path\n")
    req_time = time.strftime("%Y%m%d_%H%M%S")
    input_json_str = json.dumps(input_json_str1)
    # write request to file
    signed_input_file = ('./results/' + output_json_file_name + '_' + req_time
                         + '_request.json')
    with open(signed_input_file, 'w') as req_file:
        req_file.write(json.dumps(input_json_str, ensure_ascii=False))
        # json.dump(input_json_str1, req_file)

    logger.info('**********Received Request*********\n%s\n', input_json_str)
    # submit request and retrieve response
    response = uri_client._postmsg(input_json_str)
    logger.info('**********Received Response*********\n%s\n', response)

    # write response to file
    response_output_file = ('./results/' + output_json_file_name + '_'
                            + req_time + '_response.json')
    with open(response_output_file, 'w') as resp_file:
        resp_file.write(json.dumps(response, ensure_ascii=False))

    return response


def submit_work_order_sdk(wo_params, input_json_obj):
    logger.info("SDK code path\n")
    req_id = input_json_obj["id"]
    config = pconfig.parse_configuration_files(
        constants.conffiles, constants.confpaths)
    logger.info(" URI client %s \n", config["tcf"]["json_rpc_uri"])
    # config["tcf"]["json_rpc_uri"] = globals.uri_client
    #work_order = JRPCWorkOrderImpl(config)
    work_order = _create_work_order_instance(globals.blockchain, config)
    response = work_order.work_order_submit(
        wo_params.get_work_order_id(),
        wo_params.get_worker_id(),
        wo_params.get_requester_id(),
        wo_params.to_string(),
        id=req_id
    )
    logger.info("Work order submit response : {}\n ".format(
        json.dumps(response, indent=4)
    ))

    return response


def submit_lookup_sdk(worker_type, input_json):
    logger.info("SDK code path\n")
    jrpc_req_id = input_json["id"]
    config = pconfig.parse_configuration_files(
        constants.conffiles, constants.confpaths)
    # config["tcf"]["json_rpc_uri"] = globals.uri_client
    logger.info(" URI client %s \n", config["tcf"]["json_rpc_uri"])
    worker_dict = {'SGX': WorkerType.TEE_SGX,
                   'MPC': WorkerType.MPC, 'ZK': WorkerType.ZK}
    worker_registry = JRPCWorkerRegistryImpl(config)

    worker_lookup_response = worker_registry.worker_lookup(
        worker_type=worker_dict[worker_type], id=jrpc_req_id
    )
    logger.info("\n Worker lookup response: {}\n".format(
        json.dumps(worker_lookup_response, indent=4)
    ))

    return worker_lookup_response


def submit_retrieve_sdk(worker_id, input_json):
    logger.info("SDK code path\n")
    jrpc_req_id = input_json["id"]
    config = pconfig.parse_configuration_files(
        constants.conffiles, constants.confpaths)
    # config["tcf"]["json_rpc_uri"] = globals.uri_client
    logger.info(" URI client %s \n", config["tcf"]["json_rpc_uri"])
    worker_registry = JRPCWorkerRegistryImpl(config)
    worker_retrieve_result = worker_registry.worker_retrieve(
        worker_id, jrpc_req_id
    )
    logger.info("\n Worker retrieve response: {}\n".format(
        json.dumps(worker_retrieve_result, indent=4)
    ))

    if "error" in worker_retrieve_result:
        logger.error("Unable to retrieve worker details\n")
        sys.exit(1)

    return worker_retrieve_result


def submit_create_receipt_sdk(wo_create_receipt, input_json):
    logger.info("SDK code path\n")
    jrpc_req_id = input_json["id"]
    config = pconfig.parse_configuration_files(
        constants.conffiles, constants.confpaths)
    # config["tcf"]["json_rpc_uri"] = globals.uri_client
    logger.info(" URI client %s \n", config["tcf"]["json_rpc_uri"])
    # Create receipt
    wo_receipt = JRPCWorkOrderReceiptImpl(config)
    # Submit work order create receipt jrpc request
    wo_receipt_resp = wo_receipt.work_order_receipt_create(
        wo_create_receipt["workOrderId"],
        wo_create_receipt["workerServiceId"],
        wo_create_receipt["workerId"],
        wo_create_receipt["requesterId"],
        wo_create_receipt["receiptCreateStatus"],
        wo_create_receipt["workOrderRequestHash"],
        wo_create_receipt["requesterGeneratedNonce"],
        wo_create_receipt["requesterSignature"],
        wo_create_receipt["signatureRules"],
        wo_create_receipt["receiptVerificationKey"],
        jrpc_req_id
    )
    logger.info("Work order create receipt response : {} \n \n ".format(
        wo_receipt_resp
    ))
    return wo_receipt_resp
