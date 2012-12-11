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


%changelog
* Sat May 30 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.0-1mdv2010.0
+ Revision: 381394
- Update to new version 2.0.0
- Switch to new URL
- Builds on x86_64 too now

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Apr 20 2007 Pixel <pixel@mandriva.com> 1.4.1-4mdv2008.0
+ Revision: 16055
- rebuild
- fix url
- Import read-edid



* Fri Feb  3 2006 Pixel <pixel@mandriva.com> 1.4.1-3mdk
- it only builds on ix86 (see monitor-edid)

* Fri Feb  3 2006 Pixel <pixel@mandriva.com> 1.4.1-2mdk
- rebuild

* Sat Jul 17 2004 Frederic Lepied <flepied@mandrakesoft.com> 1.4.1-1mdk
- initial packaging

# end of file
