%define name gnome-backgrounds
%define version 2.27.91
%define release %mkrel 1

Summary: Background images for the GNOME desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: GPLv2
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: intltool
BuildArch: noarch

%description
This module contains a set of backgrounds packaged with the GNOME desktop.

%prep
%setup -q
%build
./configure --prefix=%_prefix --libdir=%_libdir
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS README AUTHORS ChangeLog
%_datadir/gnome-background-properties/
%dir %_datadir/pixmaps/backgrounds
%_datadir/pixmaps/backgrounds/gnome


