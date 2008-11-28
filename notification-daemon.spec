Summary: Notification Daemon
Name: notification-daemon
Version: 0.4.0
Release: %mkrel 1
License: GPLv2+
Group: System/Servers
Source: http://www.galago-project.org/files/releases/source/notification-daemon/notification-daemon-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://www.galago-project.org/
Provides: notify-daemon
Obsoletes: notify-daemon
Provides: virtual-notification-daemon
Conflicts:	xfce4-notifyd
Buildrequires: dbus-glib-devel
BuildRequires: libsexy-devel
BuildRequires: libwnck-devel
BuildRequires: libGConf2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libnotify-devel
BuildRequires: gstreamer0.10-devel
BuildRequires: intltool
BuildRequires: gnome-common


%description
A daemon that displays passive pop-up notifications as per the
Desktop Notifications spec (http://galago.info/specs/notification/index.php).

%prep
%setup -q

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
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %name

%postun
%clean_icon_cache hicolor

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
%_datadir/icons/hicolor/*/apps/*

