#!/bin/bash
. config_file
ValResult=''

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
echo 'Description: Script to uninstall a new package 1.3-11 and install again, when SDPTool is already installed in pre configured environment'
echo 'Aim : Package testing'
echo 'Procedure : '
echo -e '\t.Pre-configuration :'
echo -e '\t\t1. Install current SDPTool package.'
echo -e '\t.Test :'
echo -e '\t\t1. Download new package,'
echo -e '\t\t2. goto install dir,'
echo -e '\t\t3. run sdptool_uninstall.sh,'
echo -e '\t\t4. run sdptool_install.sh'
echo 'Expected Result : SDPTool packages should uninstall and install smoothly'
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

function dopreconfiguration {
	./epoch.sh INSTALL /test/SDPTool-1.3-11
}

function preconfiguration {
	echo '============================================'
	echo 'Pre configuration : START'
	echo '--------------------------------------------'
	dopreconfiguration
	echo '--------------------------------------------'
	echo 'Pre configuration : DONE'
	echo '============================================'
}

function header {
	printStartBanner 3
	printDesc
}

function testcase {
	./uninstall_script.sh /test/SDPTool-1.3-11
	if [  "$?" -eq 0 ]; then
	    ValResult=${ValResult}'0'
	else
	    ValResult=${ValResult}'1'
	fi
	./install_script.sh /test/SDPTool-1.3-11
	if [  "$?" -eq 0 ]; then
	    ValResult=${ValResult}'0'
	else
	    ValResult=${ValResult}'1'
	fi	
}

function validation {
	# validation logic to go here
	if [  "$ValResult" -eq '00' ]; then
		echo -e "\e[45m===============================================\e[0m"
		echo 'uninstall a new package 1.3-11 and install again, when SDPTool is already installed in pre configured environment.'
		printPass
		echo -e "\e[45m===============================================\e[0m"
	else
		printFail
	fi
}

function docleanup {
	./epoch.sh
}

function housekeeping {
	echo '============================================'
	echo 'Housekeeping : START'
	echo 'Housekeeping : Remove SDPTool and uninstall defusedxml'
	echo '---------------------------------------------'
	docleanup
	echo '---------------------------------------------'
	echo 'Housekeeping : DONE'
	echo '============================================'
}
function footer {
	printEndBanner 3
}
function main {
	header
	preconfiguration
	testcase
	validation
	housekeeping
	footer
}

main