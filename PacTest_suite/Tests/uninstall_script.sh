#!/usr/bin/expect -f

set path [lindex $argv 0];

set timeout -1
spawn $path/sdptool_uninstall.sh
expect "Do you wish to Uninstall the SDPTool. Note: This script will delete SDPTool install folder(Y/N) :"
send -- "Y\r"
expect eof
