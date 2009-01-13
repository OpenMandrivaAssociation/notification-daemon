Summary:	Notification Daemon
Name:		notification-daemon
Version:	0.4.0
Release:	%mkrel 3
License:	GPLv2+
Group:		System/Servers
URL:		http://www.galago-project.org/
Source0:	http://www.galago-project.org/files/releases/source/notification-daemon/%{name}-%{version}.tar.bz2
Patch:notification-daemon-0.4.0-dont-display-capplet.patch
Buildrequires:	dbus-glib-devel
BuildRequires:	libsexy-devel
BuildRequires:	libwnck-devel
BuildRequires:	libGConf2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	libnotify-devel
BuildRequires:	gstreamer0.10-devel
BuildRequires:	intltool
BuildRequires:	gnome-common
Provides:	notify-daemon
Obsoletes:	notify-daemon < %{version}
Provides:	virtual-notification-daemon
Conflicts:	xfce4-notifyd
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
A daemon that displays passive pop-up notifications as per the
Desktop Notifications spec (http://galago.info/specs/notification/index.php).

%prep
%setup -q
%patch -p1

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/%{name}-1.0/engines/*.a

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%post_install_gconf_schemas %name
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%preun
%preun_uninstall_gconf_schemas %name
%endif

%if %mdkversion < 200900
%postun
%clean_icon_cache hicolor
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/notification-properties
%{_datadir}/applications/notification-properties.desktop
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/notification-daemon.schemas
%{_libexecdir}/%{name}
%{_libdir}/notification-daemon-1.0/
%{_datadir}/dbus-1/services/*
%{_datadir}/icons/hicolor/*/apps/*
