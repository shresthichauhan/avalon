#!/bin/sh
Date=`date +%Y-%m-%d`
export RUNID="Nightly"_${Date}
DIR="/Jenkins/SDPTool/$RUNID"
mkdir -p $DIR
cd $DIR
SUB_DIR="SDPTool-1.3-11/RPMS/ubuntu_18_x/"
mkdir -p $SUB_DIR

cd /Jenkins/dcg_csw_platform_software-intelcli/build
echo "================= $NODE_NAME"
if [ "ubuntu18_x_jenkins" = "$NODE_NAME" ]; then
    echo "================= This is copy final result ===================="
    cp RPMS/SDPTool-1.3-11*.* "$DIR/$SUB_DIR"
else
    echo "================Not Copying the final result =================="
fi
