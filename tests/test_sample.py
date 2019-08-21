import logging
from encodings.hex_codec import hex_encode
import unittest #1
import toml
from os import path, environ
import errno
import secrets
import time
import base64
import json
from connectors.direct.work_order_jrpc_impl import WorkOrderJRPCImpl

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)


class WorkOrderJRPCAPI(unittest.TestCase): #2
    def __init__(self, config_file):
        logging.info("Please result configuration file to check..... %s\n", config_file)	
        super(WorkOrderJRPCAPI, self).__init__()
        if not path.isfile(config_file):
            raise FileNotFoundError("File not found at path: {0}".format(path.realpath(config_file)))
        try:
            with open(config_file) as fd:
                self.__config = toml.load(fd)
                logging.info("***self.__config*** Result: %s\n", self.__config)
        except IOError as e:
            if e.errno != errno.ENOENT:
                raise Exception("Could not open config file: %s",e)
        
        self.__work_order_wrapper = WorkOrderJRPCImpl(self.__config)

        logging.info("\n***self.__work_order_wrapper*** Result: %s\n", self.__work_order_wrapper)    		
        self.__work_order_id = secrets.token_hex(32)
        		
        #*** Use get set utility class to modify the parameter value and validate the response ***
        self.__work_order_submit_request = {
        "responseTimeoutMSecs": 6000,
        "payloadFormat": "pformat",
        "resultUri": "http://result-uri:8080",
        "notifyUri": "http://notify-uri:8080",
        "workOrderId": self.__work_order_id,
        "workerId": "",
        "workloadId": "heart-disease-eval".encode("utf-8").hex(),
        "requesterId": secrets.token_hex(32),
        "workerEncryptionKey": secrets.token_hex(32),
        "dataEncryptionAlgorithm": "AES-GCM-256",
        "encryptedSessionKey": "sessionkey".encode("utf-8").hex(),
        "sessionKeyIv": "ivSessionKey".encode("utf-8").hex(),
        "requesterNonce": "",
        "encryptedRequestHash": "requesthash".encode("utf-8").hex(),
        "requesterSignature": base64.b64encode(str.encode("SampleRequesterSignature", "utf-8")).decode("utf-8"),
     #   "verifyingKey": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEWPblapM4eJI3vg8I8DhoKAeceop2VnqK\n40Yqs6WhLpxYvbYGrDsrIwNTZHrxNSHaX59APUpWamulen25G3LFCw==\n-----END PUBLIC KEY-----\n"
        "verifyingKey":""
        }
        self.__in_data = [
            {
                "index": 1,
                "dataHash": "mhash444".encode("utf-8").hex(),
                "data": base64.b64encode(str.encode("Heart disease evaluation data: 32 1 1 156  132 125 1 95  1 0 1 1 3 1","utf-8")).decode("utf-8"),
                "encryptedDataEncryptionKey": "12345".encode("utf-8").hex(),
                "iv": "iv_1".encode("utf-8").hex()
             }
        ]
        self.__out_data = [
        {
            "index": 1,
            "dataHash": "mhash444".encode("utf-8").hex(),
            "data": base64.b64encode(str.encode("Heart disease evaluation data: 32 1 1 156  132 125 1 95  1 0 1 1 3 1","utf-8")).decode("utf-8"),
            "encryptedDataEncryptionKey": "12345".encode("utf-8").hex(),
            "iv": "iv_1".encode("utf-8").hex()
        }
        ]
    def test_work_order_submit(self):
        req_id = 21
        logging.info("Calling work_order_submit with params %s\nin_data %s\nout_data %s\n",
        json.dumps(self.__work_order_submit_request, indent=4), 
        json.dumps(self.__in_data, indent=4), 
        json.dumps(self.__out_data, indent=4))
        
        #***Concatenate all the three separate dictionary in one and sign the input.***
		
        res = self.__work_order_wrapper.work_order_submit(self.__work_order_submit_request, self.__in_data, self.__out_data, req_id)
        logging.info("Result: %s\n", res)
        self.assertEqual(res['id'], req_id, "work_order_submit Response id doesn't match")

    def test_work_order_get_result(self):
        req_id = 22
        res = {}
        logging.info("Calling work_order_get_result with workOrderId %s\n", self.__work_order_id)
        while ('result' not in res): 
            res = self.__work_order_wrapper.work_order_get_result(self.__work_order_id, req_id)
            logging.info("Result: %s\n", res)
            time.sleep(2)

        self.assertEqual(res['id'], req_id, "work_order_get_result Response id doesn't match")

def main():
    tcf_home = environ.get("TCF_HOME", "../../")
    test = WorkOrderJRPCAPI(tcf_home + "/tests/" + "test_sample.toml")	
    test.test_work_order_submit()
    test.test_work_order_get_result()
	
if __name__ == "__main__":
    main()	

