Summary:	Notification Daemon
Name:		notification-daemon
Version:	0.5.0
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Servers
URL:		http://www.galago-project.org/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
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
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}
# Really, just use gconftool for this
rm -f $RPM_BUILD_ROOT%{_bindir}/notification-properties
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/notification-daemon/notification-properties.ui
rmdir $RPM_BUILD_ROOT%{_datadir}/notification-daemon/
rm -rf $RPM_BUILD_ROOT%{_datadir}/icons


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
