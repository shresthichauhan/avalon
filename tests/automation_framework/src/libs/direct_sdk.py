from src.utilities.submit_request_utility import \
    submit_lookup_sdk, \
    submit_retrieve_sdk, submit_create_receipt_sdk, \
    submit_work_order_sdk
import logging
import os
import json
from src.worker_lookup.worker_lookup_params \
    import WorkerLookUp
from src.libs import constants
from src.work_order_receipt.work_order_receipt_params \
    import WorkOrderReceipt
from src.utilities.submit_request_utility import \
    submit_request_listener
from src.worker_retrieve.worker_retrieve_params \
    import WorkerRetrieve
from src.work_order_submit.work_order_submit_params \
    import WorkOrderSubmit
import avalon_sdk.worker.worker_details as worker
logger = logging.getLogger(__name__)


class SDKImpl():

    def worker_lookup(self):
        lookup_obj = WorkerLookUp()
        worker_type = lookup_obj.configure_data_sdk(
            input_json=None, worker_obj=None, pre_test_response=None)

        lookup_response = submit_lookup_sdk(worker_type)
        return lookup_response

    def worker_retrieve(self, lookup_response):
        worker_obj = worker.SGXWorkerDetails()
        retrieve_obj = WorkerRetrieve()
        worker_id = retrieve_obj.configure_data_sdk(
            input_json=None, worker_obj=None,
            pre_test_response=lookup_response)
        logger.info('*****Worker details Updated with Worker ID***** \
                                           \n%s\n', worker_id)
        retrieve_response = submit_retrieve_sdk(worker_id)
        logger.info('*****Worker retrieve response***** \
                                           \n%s\n', retrieve_response)
        worker_obj.load_worker(retrieve_response['result']['details'])

        return worker_obj

    def work_order_submit(self, worker_obj):
        submit_obj = WorkOrderSubmit()
        submit_request_file = os.path.join(
            constants.work_order_input_file,
            "work_order_success.json")
        submit_request_json = self.read_json(submit_request_file)
        wo_params = submit_obj.configure_data_sdk(
            input_json=submit_request_json, worker_obj=worker_obj,
            pre_test_response=None)
        submit_response = submit_work_order_sdk(wo_params)
        # input_work_order_submit = submit_obj.compute_signature(
        #    constants.wo_submit_tamper)
        logger.info("******Work Order submitted*****\n%s\n", submit_response)
        return wo_params

    def work_order_create_receipt(self, wo_submit):
        receipt_retrieve_obj = WorkOrderReceipt()
        receipt_retrieve_file = os.path.join(
            constants.work_order_receipt,
            "work_order_receipt.json")
        receipt_request_json = self.read_json(receipt_retrieve_file)
        wo_create_receipt = receipt_retrieve_obj.configure_data_sdk(
            input_json=receipt_request_json, worker_obj=None,
            pre_test_response=wo_submit)
        receipt_create_response = submit_create_receipt_sdk(
            wo_create_receipt, receipt_request_json)
        logger.info("***Receipt created***\n%s\n", receipt_create_response)
        logger.info("***Receipt request***\n%s\n", wo_create_receipt)
        return wo_create_receipt

    def read_json(self, request_file):
        # Read the method name from JSON file
        with open(request_file, "r") as file:
            input_json = file.read().rstrip('\n')

        input_json_obj = json.loads(input_json)

        return input_json_obj
