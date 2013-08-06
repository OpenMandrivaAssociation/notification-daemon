%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Notification Daemon
Name:		notification-daemon
Version:	0.7.6
Release:	1
License:	GPLv2+
Group:		System/Servers
Url:		http://www.galago-project.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/notification-daemon/%{url_ver}/%{name}-%{version}.tar.xz

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

