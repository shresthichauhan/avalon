#!/bin/bash


function printStartBanner() {
echo -e '\e[45m===============================================\e[0m'
echo "Testcase_$1"
echo 'START'
echo -e '\e[45m===============================================\e[0m'
}

function printEndBanner() {
echo -e '\e[45m===============================================\e[0m'
echo "Testcase $1"
echo 'END'
echo -e '\e[45m===============================================\e[0m'
}

function printDesc {
echo -e "\e[45m===============================================\e[0m"
echo 'Description: New SDPTool package already installed'
echo 'Aim : Package testing'
echo 'Procedure : New SDPTool package already installed'
echo 'Expected Result : New SDPTool package already installed'
echo -e "\e[45m===============================================\e[0m"
}

function printPass {
    echo '========================='
    echo 'Result : PASS'
    echo '========================='
}

function printFail {
    echo '========================='
    echo 'Result : FAIL'
    echo '========================='
}

./epoch.sh INSTALL /test/SDPTool-1.3-11

echo '============================================'
echo 'Cleaning the system before we start anything'
echo 'Housekeeping: Ready to run the test'
echo '============================================'


printStartBanner 15
printDesc


# Testcase 15 let's install the latest SDPTool
./install_script.sh /test/SDPTool-1.3-11

# validation logic to go here
if [  "$?" -eq 0 ]; then
    echo -e "\e[45m===============================================\e[0m"
    echo 'New SDPTool package already installed .'
    printPass
	echo -e "\e[45m===============================================\e[0m"
else
    printFail
fi

# Print the end banner
printEndBanner 15