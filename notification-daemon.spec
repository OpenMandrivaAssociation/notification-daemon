%define svn r3009
Summary: Notification Daemon
Name: notification-daemon
Version: 0.3.90
Release: %mkrel 0.%svn.1
License: GPLv2+
Group: System/Servers
Source: http://www.galago-project.org/files/releases/source/notification-daemon/notification-daemon-%{svn}.tar.bz2
#gw from RH: fix clipped notifications (bug #39952)
Patch2: notification-daemon-clipping.patch
Patch3: notification-daemon-svn3009-distfix.patch
Patch4: notification-daemon-positioning.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://www.galago-project.org/
Provides: notify-daemon
Obsoletes: notify-daemon
Provides: virtual-notification-daemon
Buildrequires: dbus-glib-devel
BuildRequires: libsexy-devel
BuildRequires: libwnck-devel
BuildRequires: libGConf2-devel
BuildRequires: libnotify-devel
BuildRequires: gstreamer0.10-devel
BuildRequires: intltool

%description
A daemon that displays passive pop-up notifications as per the
Desktop Notifications spec (http://galago.info/specs/notification/index.php).

%prep
%setup -q -n %name
%patch2 -p1 -b .clipping
%patch3 -p0 -b .svn3009-distfix
%patch4 -p0 -b .positioning
./autogen.sh
intltoolize --force

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/%name-1.0/engines/*.a
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas %name

%preun
%preun_uninstall_gconf_schemas %name

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%_bindir/notification-properties
%_datadir/applications/notification-properties.desktop
%_datadir/%name
%_sysconfdir/gconf/schemas/notification-daemon.schemas
%{_libexecdir}/%name
%_libdir/notification-daemon-1.0/
%{_datadir}/dbus-1/services/*


