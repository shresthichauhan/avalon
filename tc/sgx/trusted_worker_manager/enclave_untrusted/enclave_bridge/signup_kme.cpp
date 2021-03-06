/* Copyright 2020 Intel Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "enclave_u.h"

#include "error.h"
#include "avalon_sgx_error.h"
#include "log.h"
#include "tcf_error.h"
#include "types.h"

#include "signup_kme.h"
#include "enclave.h"
#include "base.h"

// XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
tcf_err_t tcf::enclave_api::enclave_data_kme::CreateEnclaveDataKME(
    const std::string& inExtData,
    const std::string& inExtDataSignature,
    StringArray& outPublicEnclaveData,
    Base64EncodedString& outSealedEnclaveData,
    Base64EncodedString& outEnclaveQuote) {
    tcf_err_t result = TCF_SUCCESS;

    try {
        tcf_err_t presult = TCF_SUCCESS;
        sgx_status_t sresult;

        size_t computed_public_enclave_data_size = 0;
        size_t computed_sealed_enclave_data_size = 0;

        // Get the enclave id for passing into the ecall
        sgx_enclave_id_t enclaveid = g_Enclave[0].GetEnclaveId();

        // Create enclave signature key and encryption key pair
        sresult = g_Enclave[0].CallSgx(
            [enclaveid,
             &presult,
             &computed_public_enclave_data_size,
             &computed_sealed_enclave_data_size] () {
                sgx_status_t ret = ecall_CreateEnclaveData(
                    enclaveid,
                    &presult,
                    &computed_public_enclave_data_size,
                    &computed_sealed_enclave_data_size);
                return tcf::error::ConvertErrorStatus(ret, presult);
            });
        tcf::error::ThrowSgxError(sresult,
            "SGX enclave call failed (ecall_CreateEnclaveData), failed to create signup data");
        g_Enclave[0].ThrowTCFError(presult);

        outPublicEnclaveData.resize(computed_public_enclave_data_size);
        ByteArray sealed_enclave_data_buffer(computed_sealed_enclave_data_size);
    
        // We need target info in order to create signup data report
        sgx_target_info_t target_info = { 0 };
        sgx_epid_group_id_t epidGroupId = { 0 };
        sresult =
            g_Enclave[0].CallSgx(
                [&target_info,
                 &epidGroupId] () {
                    return sgx_init_quote(&target_info, &epidGroupId);
                });
        tcf::error::ThrowSgxError(sresult,
            "Intel SGX enclave call failed (sgx_init_quote);"
            " failed to initialize the quote");

        // Properly size the sealed signup data buffer for the caller
        // and call into the enclave to create the signup data
        sgx_report_t enclave_report = { 0 };

        sresult = g_Enclave[0].CallSgx(
            [enclaveid,
             &presult,
             target_info,
             inExtData,
             inExtDataSignature,
             &outPublicEnclaveData,
             &sealed_enclave_data_buffer,
             &enclave_report ] () {
                sgx_status_t ret = ecall_CreateSignupDataKME(
                    enclaveid,
                    &presult,
                    &target_info,
                    (const uint8_t*) inExtData.c_str(),
                    inExtData.length(),
                    (const uint8_t*) inExtDataSignature.c_str(),
                    inExtDataSignature.length(),
                    outPublicEnclaveData.data(),
                    outPublicEnclaveData.size(),
                    sealed_enclave_data_buffer.data(),
                    sealed_enclave_data_buffer.size(),
                    &enclave_report);
                return tcf::error::ConvertErrorStatus(ret, presult);
            });
        tcf::error::ThrowSgxError(sresult,
            "Intel SGX enclave call failed (ecall_CreateSignupDataKME);"
            " failed to create signup data");
        g_Enclave[0].ThrowTCFError(presult);
        outSealedEnclaveData = \
            ByteArrayToBase64EncodedString(sealed_enclave_data_buffer);

        // Take the report generated and create a quote for it, encode it
        size_t quote_size = tcf::enclave_api::base::GetEnclaveQuoteSize();
        ByteArray enclave_quote_buffer(quote_size);
        g_Enclave[0].CreateQuoteFromReport(&enclave_report, enclave_quote_buffer);
        outEnclaveQuote = ByteArrayToBase64EncodedString(enclave_quote_buffer);
    } catch (tcf::error::Error& e) {
        tcf::enclave_api::base::SetLastError(e.what());
        result = e.error_code();
    } catch (std::exception& e) {
        tcf::enclave_api::base::SetLastError(e.what());
        result = TCF_ERR_UNKNOWN;
    } catch (...) {
        tcf::enclave_api::base::SetLastError(
            "Unexpected exception in (CreateEnclaveDataKME)");
        result = TCF_ERR_UNKNOWN;
    }

    return result;
}  // tcf::enclave_api::enclave_data_kme::CreateEnclaveDataKME

// XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
tcf_err_t tcf::enclave_api::enclave_data_kme::VerifyEnclaveInfoKME(
    const std::string& enclaveInfo,
    const std::string& mr_enclave,
    const std::string& ext_data) {
    tcf_err_t result = TCF_SUCCESS;
    try {
        // xxxxx call the enclave
        sgx_enclave_id_t enclaveid = g_Enclave[0].GetEnclaveId();
        tcf_err_t presult = TCF_SUCCESS;

        sgx_status_t sresult = g_Enclave[0].CallSgx(
            [ enclaveid,
              &presult,
              enclaveInfo,
              mr_enclave,
              ext_data ] () {
              sgx_status_t sresult =
              ecall_VerifyEnclaveInfoKME(
                             enclaveid,
                             &presult,
                             enclaveInfo.c_str(),
                             mr_enclave.c_str(),
                             (const uint8_t*) ext_data.c_str());
	      return tcf::error::ConvertErrorStatus(sresult, presult);
	});

        tcf::error::ThrowSgxError(sresult,
            "Intel SGX enclave call failed (ecall_VerifyEnclaveInfo)");
        g_Enclave[0].ThrowTCFError(presult);

    } catch (tcf::error::Error& e) {
        tcf::enclave_api::base::SetLastError(e.what());
        result = e.error_code();
    } catch (std::exception& e) {
        tcf::enclave_api::base::SetLastError(e.what());
        result = TCF_ERR_UNKNOWN;
    } catch (...) {
        tcf::enclave_api::base::SetLastError("Unexpected exception");
        result = TCF_ERR_UNKNOWN;
    }
    return result;
}  // tcf::enclave_api::enclave_data_kme::VerifyEnclaveInfoKME
