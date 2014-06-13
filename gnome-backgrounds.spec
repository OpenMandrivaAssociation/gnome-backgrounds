%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Background images for the GNOME desktop
Name:		gnome-backgrounds
Version:	3.6.0
Release:	6
License:	GPLv2
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-backgrounds/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	intltool

%description
This module contains a set of backgrounds packaged with the GNOME desktop.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README AUTHORS
%{_datadir}/gnome-background-properties/
%{_datadir}/backgrounds/*

