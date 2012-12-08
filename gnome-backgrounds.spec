Summary: Background images for the GNOME desktop
Name: gnome-backgrounds
Version: 3.6.0
Release: 1
License: GPLv2
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz
BuildArch: noarch

BuildRequires: intltool

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



%changelog
* Tue Oct  9 2012 Arkady L. Shane <ashejn@rosalinux.ru> 3.6.0-1
- update to 3.6.0

* Tue May 15 2012 Götz Waschk <waschk@mandriva.org> 3.4.2-1
+ Revision: 798942
- update to new version 3.4.2

* Sun Apr 29 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.4.1-1
+ Revision: 794394
- version update 3.4.1

* Sun Mar 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.0-1
+ Revision: 784286
- added source
- new version 3.2.0
- cleaned up spec

* Wed Sep 28 2011 Götz Waschk <waschk@mandriva.org> 2.32.0-2
+ Revision: 701630
- rebuild

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581421
- update to new version 2.32.0

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528928
- update to new version 2.30.0

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 516894
- update to new version 2.29.92

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446961
- update to new version 2.28.0

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 437457
- update to new version 2.27.91

* Tue Mar 17 2009 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 356656
- update to new version 2.24.1

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287359
- new version

* Tue Sep 09 2008 Götz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282912
- new version

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 278073
- new version

* Tue Aug 19 2008 Götz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273543
- new version

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.23.0-3mdv2009.0
+ Revision: 246379
- rebuild

* Tue Jul 22 2008 Götz Waschk <waschk@mandriva.org> 2.23.0-1mdv2009.0
+ Revision: 240490
- new version
- update license
- update deps

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183221
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89353
- new version

* Sun Jul 01 2007 Götz Waschk <waschk@mandriva.org> 2.18.3-1mdv2008.0
+ Revision: 46819
- new vresion


* Wed Nov 22 2006 Götz Waschk <waschk@mandriva.org> 2.16.2-1mdv2007.0
+ Revision: 86297
- new version
- Import gnome-backgrounds

* Wed Oct 04 2006 Götz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.0
- New version 2.16.1

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.15.92-1mdv2007.0
- New release 2.15.92

* Fri Jun 02 2006 Götz Waschk <waschk@mandriva.org> 2.14.2.1-1
- New release 2.14.2.1

* Wed May 31 2006 Götz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- New release 2.14.2

* Wed Apr 12 2006 Götz Waschk <waschk@mandriva.org> 2.14.1-1mdk
- New release 2.14.1

* Mon Mar 13 2006 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdk
- New release 2.14.0

* Wed Mar 01 2006 Götz Waschk <waschk@mandriva.org> 2.13.92-1mdk
- New release 2.13.92

* Wed Feb 15 2006 Götz Waschk <waschk@mandriva.org> 2.13.91-1mdk
- New release 2.13.91

* Tue Jan 31 2006 Götz Waschk <waschk@mandriva.org> 2.13.90-1mdk
- New release 2.13.90
- use mkrel

* Tue Nov 29 2005 Götz Waschk <waschk@mandriva.org> 2.12.2-1mdk
- New release 2.12.2

* Wed Oct 05 2005 Götz Waschk <waschk@mandriva.org> 2.12.1-1mdk
- New release 2.12.1

* Tue Sep 06 2005 Götz Waschk <waschk@mandriva.org> 2.12.0-1mdk
- New release 2.12.0

* Wed Aug 24 2005 Götz Waschk <waschk@mandriva.org> 2.11.92-1mdk
- New release 2.11.92

* Sat Jul 09 2005 G�tz Waschk <waschk@mandriva.org> 2.10.2-1mdk
- New release 2.10.2

* Tue Apr 12 2005 Götz Waschk <waschk@linux-mandrake.com> 2.10.1-1mdk
- New release 2.10.1

* Tue Mar 08 2005 Götz Waschk <waschk@linux-mandrake.com> 2.10.0-1mdk
- New release 2.10.0

* Wed Mar 02 2005 Götz Waschk <waschk@linux-mandrake.com> 2.9.92-1mdk
- New release 2.9.92

* Fri Feb 11 2005 Götz Waschk <waschk@linux-mandrake.com> 2.9.91-1mdk
- New release 2.9.91

* Wed Jan 26 2005 Goetz Waschk <waschk@linux-mandrake.com> 2.9.90-1mdk
- New release 2.9.90

* Thu Jan 13 2005 G�tz Waschk <waschk@linux-mandrake.com> 2.9.4-1mdk
- initial package

