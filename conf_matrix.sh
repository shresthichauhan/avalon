173 – ubuntu18 :
mount.cifs //ip-address/Share/Jenkins /Jenkins  -o user=administrator pwd=intel@123


=================================================================================================================================================
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

=================================================================================================================================================
19-Aug-2020

#!/bin/sh
Date=`date +%Y-%m-%d`
export RUNID="Nightly"_${Date}
DIR="/Jenkins/SDPTool/$RUNID/SDPTool-1.3-11/RPMS/"
mkdir -p $DIR
cd $DIR
UBUNTU_18="ubuntu_18_x/"
mkdir -p $UBUNTU_18
UBUNTU_16="ubuntu_16_x/"
mkdir -p $UBUNTU_16
RHEL_7="rhel7_x/"
mkdir -p $RHEL_7
centos7_x="centos7_x/"
mkdir -p $centos7_x
sles12_x="sles12_x/"
mkdir -p $sles12_x

cd /Jenkins/dcg_csw_platform_software-intelcli/build
echo `pwd`
make clean
echo "================= $NODE_NAME"

if [ "ubuntu18_x_jenkins" = "$NODE_NAME" ]; then
    echo "================= $NODE_NAME"
    echo "================= Ubuntu 18.x deb is part of release candidate  ===================="
    make rpm
    cp RPMS/SDPTool-1.3-11*.* "$DIR/$UBUNTU_18"
else
    echo "================ Other than Ubuntu 18.x deb =================="
fi

if [ "ubuntu16_x_jenkins" = "$NODE_NAME" ]; then
    #cd /Jenkins/dcg_csw_platform_software-intelcli/build
    #echo `pwd`
    #make clean
    echo "================= $NODE_NAME"
    echo "================= Ubuntu 16.x deb is part of release candidate ===================="
    make rpm
    cp RPMS/SDPTool-1.3-11*.* "$DIR/$UBUNTU_16"
else
    echo "================ Other than Ubuntu 16.x deb =================="
fi

if [ "rhel7_x_jenkins" = "$NODE_NAME" ]; then
    #cd /Jenkins/dcg_csw_platform_software-intelcli/build
    #echo `pwd`
    #make clean
    echo "================= $NODE_NAME"
    echo "================= RHEL 7.x rpm is part of release candidate ===================="
    make rpm
    cp RPMS/SDPTool-1.3-11*.* "$DIR/$RHEL_7"
else
    echo "================ Other than RHEL 7.x rpm =================="
fi

if [ "centos7_x_jenkins" = "$NODE_NAME" ]; then
    cd /Jenkins/dcg_csw_platform_software-intelcli/build
    echo `pwd`
    make clean # Clean previous results
    echo "================= $NODE_NAME"
    echo "================= centos 7.x rpm is part of release candidate ===================="
    make rpm
    cp RPMS/SDPTool-1.3-11*.* "$DIR/$centos7_x"
else
    echo "================ Other than centos 7.x rpm =================="
fi
if [ "sles12_x_jenkins" = "$NODE_NAME" ]; then
    cd /Jenkins/dcg_csw_platform_software-intelcli/build
    echo `pwd`
    make clean # Clean previous results
    echo "================= $NODE_NAME"
    echo "================= sles 12.x rpm is part of release candidate ===================="
    make rpm
    cp RPMS/SDPTool-1.3-11*.* "$DIR/$sles12_x"
else
    echo "================ Other than sles 12.x rpm =================="
fi
=======================================================================================================================================
20-Aug-2020
#Building for each node.
#umount:/Jenkins: target is busy
#cmd: fuser -cuk /Jenkins
#cmd: umount -l
#++++++++++++++++++++++++++++++++++++++

#!/bin/sh
Date=`date +%Y-%m-%d`
export RUNID="Nightly"_${Date}
DIR="/Jenkins/SDPTool/$RUNID/SDPTool-1.3-11/RPMS/"
mkdir -p $DIR
cd $DIR
UBUNTU_18="ubuntu_18_x/"
mkdir -p $UBUNTU_18
UBUNTU_16="ubuntu_16_x/"
mkdir -p $UBUNTU_16
RHEL_7="rhel7_x/"
mkdir -p $RHEL_7
centos7_x="centos7_x/"
mkdir -p $centos7_x
sles12_x="sles12_x/"
mkdir -p $sles12_x

mkdir -p /Build


cp -r /Jenkins/dcg_csw_platform_software-intelcli /Build 
cd /Build/dcg_csw_platform_software-intelcli/build

echo `pwd` "this is it"
make clean
make rpm
echo "================= $NODE_NAME"


