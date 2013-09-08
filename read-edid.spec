Summary:	Get monitor details
Name:		read-edid
Version:	3.0.0
Release:	1
URL:		http://www.polypux.org/projects/read-edid/
Source0:	http://www.polypux.org/projects/read-edid/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		System/Configuration/Other
BuildRequires:	libx86-devel
BuildRequires:	cmake
Patch0:		read-edid-3.0.0-include.patch
Patch1:		read-edid-3.0.0-sharedir.patch

%description
This package will try to read the monitor details directly from the
monitor. The program get-edid asks a VBE BIOS for the EDID data. The
program parse-edid parses the data and prints out a human readable
summary.

%package	doc
Group:		Development/Other
Requires:	%{name}-%{version}-%{release}

%description
doc files for %{name}

%prep
%setup -q
%apply_patches

%build
%cmake
%make

%install
mv get-edid.man get-edid.1
%makeinstall_std -C build

%files doc
%{_docdir}/%{name}-%{version}/*

%files
%_mandir/man1/get-edid.1.*
%_bindir/*-edid*
