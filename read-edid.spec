Summary: Get monitor details
Name: read-edid
Version: 2.0.0
Release: %mkrel 1
URL: http://www.polypux.org/projects/read-edid/
Source0: http://www.polypux.org/projects/read-edid/%{name}-%{version}.tar.gz
License: GPL
Group: System/Configuration/Other
BuildRequires: libx86-devel
BuildRoot: %{_tmppath}/%{name}-buildroot

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
