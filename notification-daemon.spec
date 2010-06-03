Summary:	Notification Daemon
Name:		notification-daemon
Version:	0.4.0
Release:	%mkrel 9
License:	GPLv2+
Group:		System/Servers
URL:		http://www.galago-project.org/
Source0:	http://www.galago-project.org/files/releases/source/notification-daemon/%{name}-%{version}.tar.bz2
Patch0:notification-daemon-0.4.0-dont-display-capplet.patch
# (fc) 0.4.0-5mdv use libcanberra instead of gstreamer for sound events
Patch1:		notification-daemon-0.4.0-libcanberra.patch
# (fc) 0.4.0-5mdv no longer use libsexy, use gtk features instead (Fedora)
Patch2:		sexy.patch
# (fc) 0.4.0-7mdv use nodoka theme by default
Patch3:		nodoka.patch
#gw from Fedora, don't crash if a new monitor is connected
#https://qa.mandriva.com/show_bug.cgi?id=59195
Patch4:		variable-monitors.patch
Buildrequires:	dbus-glib-devel
BuildRequires:	libwnck-devel
BuildRequires:	libGConf2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	libnotify-devel
BuildRequires:	libcanberra-devel
BuildRequires:	intltool
BuildRequires:	gnome-common
Provides:	notify-daemon
Obsoletes:	notify-daemon < %{version}
Provides:	virtual-notification-daemon
Conflicts:	xfce4-notifyd
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Suggests:	notification-daemon-engine-nodoka

%description
A daemon that displays passive pop-up notifications as per the
Desktop Notifications spec (http://galago.info/specs/notification/index.php).

%prep
%setup -q
%apply_patches

#needed by patches 1 & 2
libtoolize --force --copy
autoreconf

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

%preun
%preun_uninstall_gconf_schemas %name

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
