173 – ubuntu18 :
mount.cifs //ip-address/Share/Jenkins /Jenkins  -o user=administrator pwd=intel@123


#!/bin/sh
Date=`date +%Y-%m-%d`
export RUNID="Nightly"_${Date}
DIR="/Jenkins/SDPTool/$RUNID/SDPTool-1.3-11/RPMS/"
mkdir -p $DIR
cd $DIR
DISTRO="ubuntu_18_x/"
mkdir -p $DISTRO

cd /Jenkins/dcg_csw_platform_software-intelcli/build
make clean # Clean previous results
echo "================= $NODE_NAME"
if [ "ubuntu18_x_jenkins" = "$NODE_NAME" ]; then
    echo "================= This is copy final result ===================="
    make rpm
    cp RPMS/SDPTool-1.3-11*.* "$DIR/$DISTRO"
else
    echo "================Not Copying the final result =================="
fi
