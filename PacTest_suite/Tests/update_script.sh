#!/usr/bin/expect -f

set path [lindex $argv 0];

set timeout -1
spawn $path/sdptool_update.sh
send -- "q\r"
expect "Do you Accept? (Y/N)"
send -- "Y\r"
interact
expect eof
