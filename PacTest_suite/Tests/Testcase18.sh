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
echo '----------------------------------'
echo 'Description: Script to check Update to latest package and uninstall the same, when previous SDPTool install as pre-requisite.'
echo 'Aim : Package testing'
echo 'Procedure : '
echo -e '\t.Pre-configuration :'
echo -e '\t\t1. Install previous package'
echo -e '\t.Test :'
echo -e '\t\t1. Download latest package,'
echo -e '\t\t2. goto install dir,'
echo -e '\t\t3. run sdptool_update.sh'
echo -e '\t\t4. run sdptool_uninstall.sh'
echo 'Expected Result : Updated SDPTool packages uninstall smoothly.'
echo '----------------------------------'
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
	./epoch.sh INSTALL $older_version
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
	printStartBanner 18
	printDesc
}

function testcase {
	# Testcase 18 let's update and uninstall the latest SDPTool
	./update_script.sh $newer_version
	if [  "$?" -eq 0 ]; then
	    ValResult='0'
	else
	    ValResult='1'
	fi
	./uninstall_script.sh $newer_version
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
		echo 'Upgraded SDPTool package uninstalled completed.'
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
	printEndBanner 18
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
