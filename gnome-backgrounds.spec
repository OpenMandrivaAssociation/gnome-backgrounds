%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Background images for the GNOME desktop
Name:		gnome-backgrounds
Version:	47.0
Release:	1
License:	GPLv2
Group:		Graphical desktop/GNOME
Url:		https://www.gnome.org
Source0:	https://ftp.gnome.org/pub/GNOME/sources/gnome-backgrounds/%{url_ver}/%{name}-%{version}.tar.xz
Source1:  magic-forrest-driva.jxl
BuildArch:	noarch

# https://gitlab.gnome.org/GNOME/gnome-backgrounds/-/merge_requests/22
Patch0:          gnome-backgrounds-47.beta-install-lcd-rainbow.patch

BuildRequires:	intltool
BuildRequires:  meson
Requires: gdk-pixbuf2.0
Requires: librsvg2
Requires: webp-pixbuf-loader
Requires: jpeg-xl-gdk-pixbuf

%description
This module contains a set of backgrounds packaged with the GNOME desktop.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/backgrounds/gnome

%files
%doc NEWS README.md AUTHORS
%{_datadir}/gnome-background-properties/
%{_datadir}/backgrounds/*

