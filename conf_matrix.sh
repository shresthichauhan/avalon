173 – ubuntu18 :
mount.cifs //ip-address/Share/Jenkins /Jenkins  -o user=administrator pwd=intel@123

=======================================================================================================================
#!/bin/sh
Date=`date +%Y-%m-%d-%H-%M`
RUNID="Shresthi"_${Date}
LOG="/Jenkins_publish/SDPTool/$RUNID/LOGS"
DIR="/Jenkins_publish/SDPTool/$RUNID/SDPTool-1.3-11/"
SRC="/Jenkins_publish/dcg_csw_platform_software-intelcli"
RPMS=$DIR/RPMS
DOCS=$DIR/Documents/
LIC=$DIR/Licenses/

#=================================
# Create the required directories
#=================================
echo $LOG
mkdir -p $LOG
echo $DIR
mkdir -p $RPMS
cd $LOG
mkdir -p BUILD_LOG PACTEST_LOG AUTOMATION_LOG UNITTEST_LOG
cd $RPMS
mkdir -p ubuntu_18_x ubuntu_16_x rhel_7 centos7_x sles12_x

cp -r $SRC/Documents/ $DOCS
cp -r $SRC/Licenses/ $LIC
cp -r $SRC/build/InstallScripts/* $DIR

rm -rf $DOCS/*.docx $DOCS/*.doc 


==========================================================================================================================
#!/bin/sh
if [ "jenkins_server_ubuntu18.x" = "$NODE_NAME" ]; then
    Date=`date +%Y-%m-%d`
    export RUNID="Nightly"_${Date}
    DIR="/Jenkins_publish/SDPTool/$RUNID/SDPTool-1.3-11/RPMS/"
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
fi


mkdir -p /Build
cp -r /Jenkins/dcg_csw_platform_software-intelcli /Build 
cd /Build/dcg_csw_platform_software-intelcli/build
make clean
make rpm
echo "================= $NODE_NAME"

if [ "ubuntu18_x_jenkins" = "$NODE_NAME" ]; then
    echo "================= $NODE_NAME"
    echo "================= Ubuntu 18.x deb is part of release candidate  ===================="
    scp RPMS/SDPTool-1.3-11*.* root@10.190.191.155:/Jenkins_publish/SDPTool/Nightly_2020-08-20/SDPTool-1.3-11/RPMS/ubuntu_18_x
elif [ "ubuntu16_x_jenkins" = "$NODE_NAME" ]; then
    echo "================= $NODE_NAME"
    echo "================= Ubuntu 16.x deb is part of release candidate ===================="
    scp RPMS/SDPTool-1.3-11*.* root@10.190.191.155:/Jenkins_publish/SDPTool/Nightly_2020-08-20/SDPTool-1.3-11/RPMS/ubuntu_16_x
elif [ "rhel7_x_jenkins" = "$NODE_NAME" ]; then
    echo "================= $NODE_NAME"
    echo "================= RHEL 7.x rpm is part of release candidate ===================="
    scp RPMS/SDPTool-1.3-11*.* root@10.190.191.155:/Jenkins_publish/SDPTool/Nightly_2020-08-20/SDPTool-1.3-11/RPMS/rhel7_x
elif [ "centos7_x_jenkins" = "$NODE_NAME" ]; then
    echo "================= $NODE_NAME"
    echo "================= centos 7.x rpm is part of release candidate ===================="
    scp RPMS/SDPTool-1.3-11*.* root@10.190.191.155:/Jenkins_publish/SDPTool/Nightly_2020-08-20/SDPTool-1.3-11/RPMS/centos7_x
else
    if [ "sles12_x_jenkins" = "$NODE_NAME" ]; then
        echo "================= $NODE_NAME"
        echo "================= sles 12.x rpm is part of release candidate ===================="
        scp RPMS/SDPTool-1.3-11*.* root@10.190.191.155:/Jenkins_publish/SDPTool/Nightly_2020-08-20/SDPTool-1.3-11/RPMS/sles12_x
    fi
fi


if [ "jenkins_server_ubuntu18.x" = "$NODE_NAME" ]; then
    cp -r /Jenkins_publish/dcg_csw_platform_software-intelcli/Documents/ /Jenkins_publish/SDPTool/Nightly_2020-08-20/SDPTool-1.3-11/Documents/
    cp -r /Jenkins_publish/dcg_csw_platform_software-intelcli/Licenses/ /Jenkins_publish/SDPTool/Nightly_2020-08-20/SDPTool-1.3-11/Licenses/
    cp /Jenkins_publish/dcg_csw_platform_software-intelcli/build/InstallScripts/* /Jenkins_publish/SDPTool/Nightly_2020-08-20/SDPTool-1.3-11/
    cd /Jenkins_publish/SDPTool/Nightly_2020-08-20/
    tar czvf SDPTool-1.3-11.tar.gz SDPTool-1.3-11/
fi

=================================================================================================================================================


=================================================================================================================================================



=======================================================================================================================================
20-Aug-2020
#Building for each node.
#umount:/Jenkins: target is busy
#cmd: fuser -cuk /Jenkins
#cmd: umount -l
#++++++++++++++++++++++++++++++++++++++

