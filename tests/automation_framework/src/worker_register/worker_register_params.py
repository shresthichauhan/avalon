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

import json
import logging
import secrets
logger = logging.getLogger(__name__)


class WorkerRegister():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerRegister", "id": 10}
        self.params_obj = {}
        self.details_obj = {}
        self.worker_type_data_obj = {}
        self.request_mode = "file"
        self.tamper = {"params": {}}
        self.output_json_file_name = "worker_register"
        self.worker_id  = secrets.token_hex(32)
        self.organization_id = secrets.token_hex(32)
        self.application_type_id = secrets.token_hex(32)

    def add_json_values(self, input_json_temp, worker_obj, tamper):
        for keys in input_json_temp["params"].keys():
            if "workerId" in keys:
                if input_json_temp["params"]["workerId"] != "":
                    self.set_worker_id(input_json_temp["params"]["workerId"])
                else:
                    self.set_worker_id(self.worker_id)

            elif "id" in keys:
                self.set_request_id(input_json_temp["id"])

            elif "workerType" in keys:
                if input_json_temp["params"]["workerType"] != "":
                    self.set_worker_type(input_json_temp["params"]["workerType"])
                else:
                    self.set_worker_type(1)

            elif "organizationId" in keys:
                if input_json_temp["params"]["organizationId"] != "":
                    self.set_organizationId(
                        input_json_temp["params"]["organizationId"])
                else:
                    self.set_organizationId(self.organization_id)

            elif "applicationTypeId" in keys:
                if input_json_temp["params"]["applicationTypeId"] != "":
                    self.set_applicationTypeId(
                        input_json_temp["params"]["applicationTypeId"])
                else:
                    self.set_applicationTypeId(self.application_type_id)

            elif "workerEncryptionKey" in keys:
                if input_json_temp["params"]["workerEncryptionKey"] != "":
                    self.set_workerEncryptionKey(
                        input_json_temp["params"]["workerEncryptionKey"])
                else:
                    self.set_workerEncryptionKey(worker_obj.worker_encryption_key)

            elif "details" in keys:
                for keys in input_json_temp["params"]["details"].keys():
                    if "hashingAlgorithm" in keys:
                        self.set_hashing_algorithm(
                            input_json_temp["params"]["details"]
                            ["hashingAlgorithm"])

                    elif "signingAlgorithm" in keys:
                        self.set_signing_algorithm(
                            input_json_temp["params"]["details"]
                            ["signingAlgorithm"])

                    elif "keyEncryptionAlgorithm" in keys:
                        self.set_key_encryption_algorithm(
                            input_json_temp["params"]["details"]
                            ["keyEncryptionAlgorithm"])

                    elif "dataEncryptionAlgorithm" in keys:
                        self.set_data_encryption_algorithm(
                            input_json_temp["params"]["details"]
                            ["dataEncryptionAlgorithm"])

                    elif "workOrderPayloadFormats" in keys:
                        self.set_workOrder_Payload_Formats(
                            input_json_temp["params"]["details"]
                            ["workOrderPayloadFormats"])

                    elif "workerTypeData" in keys:
                        for keys in input_json_temp["params"]["details"]["workerTypeData"].keys():
                            if "verificationKey" in keys:
                                self.set_verification_key(
                                    input_json_temp["params"]["details"]
                                    ["workerTypeData"]["verificationKey"])

                            elif "encryptionKey" in keys:
                                self.set_encryption_key(
                                    input_json_temp["params"]["details"]
                                    ["workerTypeData"]["encryptionKey"])

                            elif "encryptionKeyNonce" in keys:
                                self.set_encryption_key_nonce(
                                    input_json_temp["params"]["details"]
                                    ["workerTypeData"]["encryptionKeyNonce"])

                            elif "encryptionKeySignature" in keys:
                                self.set_encryption_key_signature(
                                    input_json_temp["params"]["details"]
                                    ["workerTypeData"]["encryptionKeySignature"])

                            elif "enclaveCertificate" in keys:
                                self.set_enclave_certificate(
                                    input_json_temp["params"]["details"]
                                    ["workerTypeData"]["enclaveCertificate"])

                    else:
                        for key in tamper["params"].keys():
                            param = key
                            value = tamper["params"][key]
                            self.set_unknown_parameter(param, value)

    def set_unknown_parameter(self, param, value):
        self.params_obj[param] = value

    def set_worker_id(self, worker_id):
        self.params_obj["workerId"] = worker_id

    def set_organizationId(self, organizationId):
        self.params_obj["organizationId"] = organizationId

    def set_applicationTypeId(self, applicationTypeId):
        self.params_obj["applicationTypeId"] = applicationTypeId

    def set_workerEncryptionKey(self, workerEncryptionKey):
        self.params_obj["workerEncryptionKey"] = workerEncryptionKey

    def set_worker_type(self, worker_type):
        self.params_obj["workerType"] = worker_type

    def set_request_id(self, request_id):
        self.id_obj["id"] = request_id

    def set_hashing_algorithm(self, hashing_algorithm):
        self.details_obj["hashingAlgorithm"] = hashing_algorithm

    def set_signing_algorithm(self, signing_algorithm):
        self.details_obj["signingAlgorithm"] = signing_algorithm

    def set_key_encryption_algorithm(self, key_encryption_algorithm):
        self.details_obj["keyEncryptionAlgorithm"] = key_encryption_algorithm

    def set_data_encryption_algorithm(self, data_encryption_algorithm):
        self.details_obj["dataEncryptionAlgorithm"] = data_encryption_algorithm

    def set_verification_key(self, verification_key):
        self.worker_type_data_obj["verificationKey"] = verification_key

    def set_encryption_key(self, encryption_key):
        self.worker_type_data_obj["encryptionKey"] = encryption_key

    def set_encryption_key_nonce(self, encryption_key_nonce):
        self.worker_type_data_obj["encryptionKeyNonce"] = encryption_key_nonce

    def set_encryption_key_signature(self, encryption_key_signature):
        self.worker_type_data_obj["encryptionKeySignature"] = encryption_key_signature

    def set_enclave_certificate(self, enclave_certificate):
        self.worker_type_data_obj["enclaveCertificate"] = enclave_certificate

    def set_workOrder_Payload_Formats(self, workOrder_payload_formats):
        self.details_obj["workOrderPayloadFormats"] = workOrder_payload_formats        

    def get_params(self):
        return self.params_obj.copy()

    def get_details(self):
        return self.details_obj.copy()

    def get_worker_type_data_obj(self):
        return self.worker_type_data_obj.copy()

    def to_string(self):
        json_rpc_request = self.id_obj
        json_rpc_request["params"] = self.get_params()
        json_rpc_request["params"]["details"] = self.get_details()
        json_rpc_request["params"]["details"]["workerTypeData"] = self.get_worker_type_data_obj()

        return json.dumps(json_rpc_request, indent=4)

    def configure_data(
            self, input_json, worker_obj, pre_test_response):
        logger.info(" Request json %s \n", input_json)
        self.add_json_values(input_json, worker_obj, self.tamper)
        final_json = json.loads(self.to_string())
        logger.info(" Final json %s \n", final_json)
        return final_json

    def configure_data_sdk(
            self, input_json, worker_obj, pre_test_response):
        organization_id = ""
        application_type_id = ""
        if "workerId" in input_json["params"].keys():
            if input_json["params"]["workerId"] == "":
                worker_id = self.worker_id
            else:
                worker_id = input_json["params"]["workerId"]
        if "organizationId" in input_json["params"].keys():
            if input_json["params"]["organizationId"] == "":
                organization_id = self.organization_id
            else:
                organization_id = input_json["params"]["organizationId"]
        if "applicationTypeId" in input_json["params"].keys():
            if input_json["params"]["applicationTypeId"] == "":
                application_type_id = self.application_type_id
            else:
                application_type_id = input_json["params"]["applicationTypeId"]
        if "workerType" in input_json["params"].keys():
            workerType = 'SGX'
        if "details" in input_json["params"].keys():
            details = input_json["params"]["details"]
        register_params = {"worker_id": worker_id, "workerType": workerType,
                "organization_id": organization_id, "application_type_id": application_type_id,
                "details": details}
        return register_params
