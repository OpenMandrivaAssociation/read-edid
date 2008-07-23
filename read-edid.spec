%define name read-edid
%define version 1.4.1
%define release %mkrel 6

Summary: Get monitor details
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://john.fremlin.de/programs/linux/read-edid
Source0: http://john.fremlin.de/programs/linux/read-edid/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Configuration/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
Exclusivearch: %ix86

%description
This package will try to read the monitor details directly from the
monitor. The program get-edid asks a VBE BIOS for the EDID data. The
program parse-edid parses the data and prints out a human readable
summary.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_mandir/*/*
%_sbindir/*
