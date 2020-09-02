

function print_test_case()
{
    echo -e "\e[45m===============================================\e[0m"
    echo "Test_case_$1"
    echo -e "\e[45m===============================================\e[0m"
}
function print_test_case_complete()
{
    echo -e "\e[45m===============================================\e[0m"
    echo "Test_case_complete$1"
    echo -e "\e[45m===============================================\e[0m"
}

echo "Pre_uninstall"
rm -rf SDPTool-1.3-10
tar -xvf SDPTool-1.3-10.tar.gz
cd SDPTool-1.3-10
./sdptool_uninstall.sh

print_test_case 1
cd /root/olderversion
rm -rf SDPTool-1.3-10
tar -xvf SDPTool-1.3-10.tar.gz
cd SDPTool-1.3-10
./sdptool_install.sh
cd /root/Release_candiate9
rm -rf SDPTool-1.3-11
tar -xvf SDPTool-1.3-11.tar.gz
cd SDPTool-1.3-11
./sdptool_install.sh
print_test_case_complete 1 
./sdptool_uninstall.sh






print_test_case 2
cd /root/Release_candiate9
rm -rf SDPTool-1.3-11
tar -xvf SDPTool-1.3-11.tar.gz
cd SDPTool-1.3-11
./sdptool_install.sh
./sdptool_install.sh
print_test_case_complete 2
./sdptool_uninstall.sh








print_test_case 3
cd /root/olderversion
rm -rf SDPTool-1.3-10
tar -xvf SDPTool-1.3-10.tar.gz
cd SDPTool-1.3-10
./sdptool_install.sh
cd /root/Release_candiate9
rm -rf SDPTool-1.3-11
tar -xvf SDPTool-1.3-11.tar.gz
cd SDPTool-1.3-11
./sdptool_uninstall.sh
print_test_case_complete 3











print_test_case 4
cd /root/Release_candiate9
rm -rf SDPTool-1.3-11
tar -xvf SDPTool-1.3-11.tar.gz
cd SDPTool-1.3-11
./sdptool_uninstall.sh
print_test_case_complete 4







print_test_case 5
cd /root/Release_candiate9
rm -rf SDPTool-1.3-11
tar -xvf SDPTool-1.3-11.tar.gz
cd SDPTool-1.3-11
./sdptool_update.sh
print_test_case_complete 5






print_test_case 6
cd /root/Release_candiate9
rm -rf SDPTool-1.3-11
tar -xvf SDPTool-1.3-11.tar.gz
cd SDPTool-1.3-11
./sdptool_install.sh
./sdptool_update.sh
print_test_case_complete 6








print_test_case 7
cd /root/olderversion
rm -rf SDPTool-1.3-10
tar -xvf SDPTool-1.3-10.tar.gz
cd SDPTool-1.3-10
./sdptool_install.sh
print_test_case_complete 7











print_test_case 8
cd /root/olderversion
rm -rf SDPTool-1.3-10
tar -xvf SDPTool-1.3-10.tar.gz
cd SDPTool-1.3-10
./sdptool_uninstall.sh
print_test_case_complete 8








print_test_case 9
cd /root/olderversion
rm -rf SDPTool-1.3-10
tar -xvf SDPTool-1.3-10.tar.gz
cd SDPTool-1.3-10
./sdptool_install.sh
cd /root/Release_candiate9
rm -rf SDPTool-1.3-11
tar -xvf SDPTool-1.3-11.tar.gz
cd SDPTool-1.3-11
./sdptool_update.sh
print_test_case_complete 9
./sdptool_uninstall.sh













echo "Test_case_10"
cd /root/Release_candiate9
rm -rf SDPTool-1.3-11
tar -xvf SDPTool-1.3-11.tar.gz
cd SDPTool-1.3-11
./sdptool_install.sh
print_test_case_complete 10










print_test_case 11
SDPTool -h
print_test_case_complete 11


