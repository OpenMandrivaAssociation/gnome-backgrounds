%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Background images for the GNOME desktop
Name:		gnome-backgrounds
Version:	3.38.0
Release:	1
License:	GPLv2
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-backgrounds/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:  meson

%description
This module contains a set of backgrounds packaged with the GNOME desktop.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%doc NEWS README.md AUTHORS
%{_datadir}/gnome-background-properties/
%{_datadir}/backgrounds/*

