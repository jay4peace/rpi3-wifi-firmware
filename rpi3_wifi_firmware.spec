%define _binaries_in_noarch_packages_terminate_build 0
%global _firmwarepath   /lib/firmware/brcm

Name:          rpi3-wifi-firmware
Version:       0.0
Release:       1
Summary:       rpi3 brcm firmware for WiFi
License:       Proprietary and GPL-2
BuildArch:     noarch

SOURCE0: GPL-2
SOURCE1: LICENCE.broadcom_bcm43xx
SOURCE2: brcmfmac43455-sdio.txt
SOURCE3: brcmfmac43430-sdio.bin
SOURCE4: brcmfmac43430-sdio.txt
SOURCE5: brcmfmac43455-sdio.bin

%description
rpi3 brcm firmware for WiFi

%prep
cp %{SOURCE1} LICENCE.GPL-2
cp %{SOURCE1} LICENCE.broadcom_bcm43xx

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_firmwarepath}/
install %{SOURCE2} %{buildroot}%{_firmwarepath}/
install %{SOURCE3} %{buildroot}%{_firmwarepath}/
install %{SOURCE4} %{buildroot}%{_firmwarepath}/
install %{SOURCE5} %{buildroot}%{_firmwarepath}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%license LICENCE.broadcom_bcm43xx
%license LICENCE.GPL-2
%{_firmwarepath}/*
