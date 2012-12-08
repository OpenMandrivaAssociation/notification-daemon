Summary:	Notification Daemon
Name:		notification-daemon
Version:	0.7.6
Release:	1
License:	GPLv2+
Group:		System/Servers
URL:		http://www.galago-project.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/notification-daemon/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(x11)

Provides:	virtual-notification-daemon
Conflicts:	xfce4-notifyd

Suggests:	notification-daemon-engine-nodoka
Requires(post,preun):	GConf2

%description
A daemon that displays passive pop-up notifications as per the
Desktop Notifications spec (http://galago.info/specs/notification/index.php).

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_libexecdir}/%{name}
%{_datadir}/applications/*.desktop


%changelog
* Tue Sep 04 2012 Götz Waschk <waschk@mandriva.org> 0.7.6-1
+ Revision: 816308
- update to new version 0.7.6
- fix source URL for mdvsys

* Mon Jul 09 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.5-1
+ Revision: 808639
- update to new version 0.7.5

* Sat May 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.7.4-1
+ Revision: 796412
- new version 0.7.4

* Thu May 05 2011 Funda Wang <fwang@mandriva.org> 0.5.0-3
+ Revision: 669314
- fix build with notify 0.7
- libsm is not needed now

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Tue Dec 14 2010 Götz Waschk <waschk@mandriva.org> 0.5.0-2mdv2011.0
+ Revision: 621701
- update build deps
- remove notification-properties like Fedora did
- add deps for gconf schema installation (bug #61302)

  + John Balcaen <mikala@mandriva.org>
    - Fix BR for libcanberra-gtk-devel

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2011.0
+ Revision: 550637
- new version
- drop all patches
- update build deps

* Thu Jun 03 2010 Götz Waschk <waschk@mandriva.org> 0.4.0-9.r3038.1mdv2010.1
+ Revision: 547010
- use latest svn snapshot to prevent crash (bug #59615)
- rediff 1
- add patches from Fedora:
 * use the right web browser
 * use right check for running screensaver
- fix rpm scripts

* Sat May 15 2010 Götz Waschk <waschk@mandriva.org> 0.4.0-9mdv2010.1
+ Revision: 544851
- fix dual monitor crash (bug #59195)

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-8mdv2010.1
+ Revision: 523438
- rebuilt for 2010.1

* Fri Sep 25 2009 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-7mdv2010.0
+ Revision: 448897
- Use nodoka theme by default

* Tue Sep 08 2009 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-6mdv2010.0
+ Revision: 433390
- Really remove gstreamer dependency

* Tue Sep 08 2009 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-5mdv2010.0
+ Revision: 433140
- Patch1: use libcanberra instead of gstreamer to play sound events
- Patch2 (Fedora): use new gtk features instead of libsexy

* Fri Jun 05 2009 Götz Waschk <waschk@mandriva.org> 0.4.0-4mdv2010.0
+ Revision: 382964
- requires gstreamer base plugins (bug #51311)

* Tue Jan 13 2009 Götz Waschk <waschk@mandriva.org> 0.4.0-3mdv2009.1
+ Revision: 328998
- hide configuration applet by default (bug #46651)

* Fri Nov 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-2mdv2009.1
+ Revision: 307478
- spec file clean
- do not run scriplets for mdv 200900 and newer
- do not package COPYING file
- do not selfobsolete at notify-deamon
- do not provide/obsolete notification-deamon-xfce
- add conflicts against xfce4-notifyd

* Thu Nov 20 2008 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2009.1
+ Revision: 305259
- new version
- drop patches
- drop extra icons

* Tue Nov 18 2008 Thierry Vignaud <tv@mandriva.org> 0.3.90-0.r3017.2mdv2009.1
+ Revision: 304208
- fix upgrading from XFCE-4.2

* Fri Sep 26 2008 Götz Waschk <waschk@mandriva.org> 0.3.90-0.r3017.1mdv2009.0
+ Revision: 288535
- new snapshot
- drop patch 4

* Thu Sep 25 2008 Götz Waschk <waschk@mandriva.org> 0.3.90-0.r3009.2mdv2009.0
+ Revision: 288087
- add icons for notification-properties (bug #43346)

* Thu Aug 28 2008 Götz Waschk <waschk@mandriva.org> 0.3.90-0.r3009.1mdv2009.0
+ Revision: 276851
- update build deps
- update file list
- new svn snapshot
- drop patch 0
- add fedora patches to fix build and positioning of the bubbles
- update license

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.3.7-5mdv2009.0
+ Revision: 265199
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 10 2008 Götz Waschk <waschk@mandriva.org> 0.3.7-4mdv2009.0
+ Revision: 192546
- patch for bug #39952 (clipped notification text)

* Mon Mar 17 2008 Götz Waschk <waschk@mandriva.org> 0.3.7-3mdv2008.1
+ Revision: 188242
- patch to support markup in summaries

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.3.7-2mdv2008.1
+ Revision: 153286
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Wed Feb 28 2007 Jérôme Soyer <saispo@mandriva.org> 0.3.7-1mdv2007.0
+ Revision: 126929
- New release 0.3.7

* Sat Jan 13 2007 Götz Waschk <waschk@mandriva.org> 0.3.6-4mdv2007.1
+ Revision: 108283
- bump release

* Sat Jan 13 2007 Götz Waschk <waschk@mandriva.org> 0.3.6-3mdv2007.1
+ Revision: 108200
- use the right macros

* Wed Jan 10 2007 Jérôme Soyer <saispo@mandriva.org> 0.3.6-2mdv2007.1
+ Revision: 107076
- Add Provides

* Wed Nov 08 2006 Colin Guthrie <cguthrie@mandriva.org> 0.3.6-1mdv2007.0
+ Revision: 78548
- Patch to fix dbus-binding-tool usage
- New Release
- Import notification-daemon

* Sat Aug 05 2006 Götz Waschk <waschk@mandriva.org> 0.3.5-3mdv2007.0
- fix buildrequires

* Wed Aug 02 2006 Frederic Crozat <fcrozat@mandriva.com> 0.3.5-2mdv2007.0
- Rebuild with latest dbus

* Thu Apr 27 2006 Götz Waschk <waschk@mandriva.org> 0.3.5-1mdk
- New release 0.3.5

* Thu Mar 16 2006 Götz Waschk <waschk@mandriva.org> 0.3.4-2mdk
- rebuild for new libsexy

* Sun Feb 05 2006 Götz Waschk <waschk@mandriva.org> 0.3.4-1mdk
- New release 0.3.4

* Fri Jan 27 2006 Götz Waschk <waschk@mandriva.org> 0.3.3-3mdk
- fix buildrequires

* Thu Jan 26 2006 Götz Waschk <waschk@mandriva.org> 0.3.3-2mdk
- fix buildrequires

* Thu Jan 26 2006 Götz Waschk <waschk@mandriva.org> 0.3.3-1mdk
- drop patch
- New release 0.3.3

* Wed Jan 25 2006 Götz Waschk <waschk@mandriva.org> 0.3.2-1mdk
- add gconf handling
- update file list
- fix engines directory
- obsolete the ill-fated notify-daemon
- New release 0.3.2
- use mkrel

* Fri Nov 25 2005 Götz Waschk <waschk@mandriva.org> 0.2.4-1mdk
- fix buildrequires
- New release 0.2.4

* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 0.2.2-2mdk
- fix buildrequires

* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 0.2.2-1mdk
- initial mdk package

* Wed Jul 13 2005 Richard Hughes <richard@hughsie.com> 0.0.1-1
- initial packaging of 0.0.1

