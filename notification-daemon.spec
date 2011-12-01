Summary:	Notification Daemon
Name:		notification-daemon
Version:	0.5.0
Release:	%mkrel 3
License:	GPLv2+
Group:		System/Servers
URL:		http://www.galago-project.org/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch0:		notification-daemon-0.5.0-libnotify-0.7.patch
Buildrequires:	dbus-glib-devel
BuildRequires:	libwnck-devel
BuildRequires:	libGConf2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libnotify-devel
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	intltool
Provides:	notify-daemon
Obsoletes:	notify-daemon < %{version}
Provides:	virtual-notification-daemon
Conflicts:	xfce4-notifyd
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Suggests:	notification-daemon-engine-nodoka
Requires(post): GConf2
Requires(preun): GConf2

%description
A daemon that displays passive pop-up notifications as per the
Desktop Notifications spec (http://galago.info/specs/notification/index.php).

%prep
%setup -q
%apply_patches

%build
%configure2_5x --disable-static --disable-schemas-install
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}
# Really, just use gconftool for this
rm -f %{buildroot}%{_bindir}/notification-properties
rm -f %{buildroot}%{_datadir}/applications/*.desktop
rm -f %{buildroot}%{_datadir}/notification-daemon/notification-properties.ui
rmdir %{buildroot}%{_datadir}/notification-daemon/
rm -rf %{buildroot}%{_datadir}/icons


%clean
rm -rf %{buildroot}

%preun
%preun_uninstall_gconf_schemas %name

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_sysconfdir}/gconf/schemas/notification-daemon.schemas
%{_libexecdir}/%{name}
%{_libdir}/notification-daemon-1.0/
%{_datadir}/dbus-1/services/*
