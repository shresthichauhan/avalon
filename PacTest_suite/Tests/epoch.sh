#!/bin/bash

# This should clean the system such that it should be epoch in terms sdptool installed.
# In other words, remove SDPTool and it's dependencies

if [[ $1 == 'INSTALL' ]] ; then
    ./install_script.sh $2
else 
    echo 'epoch: Remove SDPTool and uninstall defusedxml'
    yum remove -y SDPTool
    pip uninstall -y defusedxml
fi

