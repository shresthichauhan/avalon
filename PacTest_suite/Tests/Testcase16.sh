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
echo 'Description: Script to check installion of previous SDPTool, when latest SDPTool installed as pre-requisite'
echo 'Aim : Package testing'
echo 'Procedure : '
echo -e '\t.Pre-configuration :'
echo -e '\t\t1. Install latest package'
echo -e '\t.Test :'
echo -e '\t\t1. Download previous package,'
echo -e '\t\t2. goto install dir,'
echo -e '\t\t3. run sdptool_install.sh'
echo 'Expected Result : Latest SDPTool already installed'
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
	./epoch.sh INSTALL $newer_version
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
	printStartBanner 16
	printDesc
}


function testcase {
	# Testcase 16 let's install the SDPTool
	./install_script.sh $older_version
	if [  "$?" -eq 0 ]; then
	    ValResult='0'
	else
	    ValResult='1'
	fi
}

function validation {
	# validation logic to go here
	if [  "$ValResult" -eq '1' ]; then
		echo -e "\e[45m===============================================\e[0m"
		echo 'Latest SDPTool package already installed.'
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
	printEndBanner 16
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