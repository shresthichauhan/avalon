Name:           SDPTool
Version:        %{ver}
Release:        %{build}%{?dist}
Summary:        Intel(R) Server Debug and Provisioning Tool
URL:            https://www.intel.com
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       ipmitool curl wget icedtea-web python-requests
License:        Intel(R) Proprietary License
Group:          Application/System
AutoReq:        no

%define prefix /usr/local/SDPTool

%description
Intel Server Debug and Provisioning Tool

%install
tar xf %{src}/SDPTool-%{version}.tar.gz -C %{buildroot}

mkdir -p %{buildroot}/usr/share/doc/SDPTool/Licenses
mkdir -p %{buildroot}/usr/local/SDPTool
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/local/log/SDPTool

# Tools
cp -r %{buildroot}/SDPTool-%{version}/*  %{buildroot}/usr/local/SDPTool/

# Documents
cp %{src}/../Licenses/* %{buildroot}/usr/share/doc/SDPTool/Licenses/.
cp %{src}/../Documents/ReleaseNotes.txt %{buildroot}/usr/share/doc/SDPTool/.
cp %{src}/../Documents/*.pdf %{buildroot}/usr/share/doc/SDPTool/.

mv %{buildroot}/usr/local/SDPTool/README.txt %{buildroot}/usr/share/doc/SDPTool/README

rm -rf %{buildroot}/usr/local/SDPTool/*.txt
rm -rf %{buildroot}/usr/local/SDPTool/Logfiles

chmod 744 %{buildroot}/usr/local/SDPTool/SDPTool
ln -sf /usr/local/SDPTool/SDPTool %{buildroot}/usr/bin/SDPTool

rm -rf %{buildroot}/SDPTool-%{version}
chmod -R 744 %{buildroot}/usr/local/log/SDPTool

%post
chmod 755 %{prefix}/VMCLI/Linux*/VMCLI*
chmod 755 %{prefix}/VMCLI2
mv /usr/share/doc/SDPTool/SDPTool_UserGuide_Rev.pdf /usr/share/doc/SDPTool/SDPTool_UserGuide_Rev_%{ver}-%{build}.pdf
chmod 755 %{prefix}/VMViewer.*
LIB=`ldd --version | awk '/ldd/{print $NF}' | awk '{split($0,a,".");} {print  a[1] "." a[2]}'`
veri=`bc <<< "$LIB < 2.16"`

if [ $veri == "1" ]
then
    cp %{prefix}/glibc_215/* %{prefix}
fi

%preun
mv /usr/share/doc/SDPTool/SDPTool_UserGuide_Rev_%{ver}-%{build}.pdf /usr/share/doc/SDPTool/SDPTool_UserGuide_Rev.pdf
rm -rf /usr/local/SDPTool/iso_*.xml
rm -rf /usr/local/SDPTool/*.log
rm -rf /usr/local/SDPTool/vmcli*_*

if [ -d /usr/local/SDPTool/mountc_* ]
then
    umount /usr/local/SDPTool/mountc_* 2>/dev/null
    rm -rf /usr/local/SDPTool/mount_*
fi

if [ -f /usr/local/SDPTool/activec_* ]
then
    rm -rf /usr/local/SDPTool/activec_*
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

/usr/local/SDPTool/
/usr/bin/SDPTool
/usr/share/doc/SDPTool/
/usr/local/log/SDPTool/

%doc

%changelog
