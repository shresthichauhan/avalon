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
echo 'Description: Install latest SDPTool after completing one package testing cycle'
echo 'Aim : Package testing'
echo 'Procedure : '
echo -e '\t.Pre-configuration :'
echo -e '\t\t1. No pre-configuration required'
echo -e '\t.Test :'
echo -e '\t\t1. Download latest package,'
echo -e '\t\t2. goto install dir,'
echo -e '\t\t3. run sdptool_install.sh'
echo 'Expected Result : After check negative scenarios, old packages installation and same to update, check new version'
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
		echo 'no pre configuration required'
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
	printStartBanner 12
	printDesc
}

function testcase {
	# Testcase 12 let's install the SDPTool	
	./install_script.sh $newer_version
	if [  "$?" -eq 0 ]; then
	    ValResult='0'
	else
	    ValResult='1'
	fi
}

function validation {
	# validation logic to go here
	if [  "$ValResult" -eq '0' ]; then
		echo -e "\e[45m===============================================\e[0m"
		echo 'After check negative scenarios, old packages installation and same to update, check new version'
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
	printEndBanner 12
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