%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	Notification Daemon
Name:		notification-daemon
Version:	3.20.0
Release:	3
License:	GPLv2+
Group:		System/Servers
Url:		https://www.galago-project.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/notification-daemon/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:  pkgconfig(gio-2.0) 
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(x11)

Provides:	virtual-notification-daemon

Suggests:	notification-daemon-engine-nodoka

%description
A daemon that displays passive pop-up notifications as per the
Desktop Notifications spec (http://galago.info/specs/notification/index.php).

%prep
%setup -q
%autopatch -p1

%build
%configure
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_libexecdir}/%{name}
%{_datadir}/applications/*.desktop

# From MGA. 
# ovitters: DO NOT PACKAGE THIS!
#           A desktop should start this explicitly themselves else it'll break
#           anything that already handles noticiations, such as e.g. GNOME
%exclude %{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
