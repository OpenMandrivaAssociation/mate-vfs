%define	api	2
%define	major	0
%define	libname	%mklibname %{name} %{api} %{major}
%define	devname %mklibname -d %{name}

Summary:	MATE virtual file-system libraries
Name:		mate-vfs
Version:	1.4.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		https://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libssl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-mime-data-2.0)
BuildRequires:	pkgconfig(smbclient)

Requires(post,preun):	mate-conf
Requires:	mate-mime-data
Requires:	shared-mime-info

%description
The MATE Virtual File System provides an abstraction to common file
system operations like reading, writing and copying files, listing
directories and so on.  It is similar in spirit to the Midnight
Commander's VFS (as it uses a similar URI scheme) but it is designed
from the ground up to be extensible and to be usable from any
application.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the library for %{name}.

%package -n %{devname}
Summary:	Development Library and include files for %{name}
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package includes libraries and header files for developing
MATE VFS applications.

%prep
%setup -q
%autopatch -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--disable-hal \
	--enable-samba \
	--enable-avahi \
	--disable-howl \
	--enable-openssl \
	--disable-gnutls

%make

%install
%makeinstall_std

%find_lang %{name}

%files -n %{name} -f %{name}.lang
%doc AUTHORS NEWS README
%config(noreplace) %{_sysconfdir}/%{name}-*
%config(noreplace) %{_sysconfdir}/mateconf/schemas/*
%{_bindir}/*
%{_datadir}/dbus-1/services/*.service
%dir %{_libdir}/%{name}-2.0
%dir %{_libdir}/%{name}-2.0/modules
%{_libdir}/%{name}-2.0/modules/*.so
%{_libexecdir}/mate-vfs-daemon

%files -n %{libname}
%{_libdir}/libmatevfs-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%dir %{_includedir}/mate-vfs-2.0
%{_includedir}/mate-vfs-2.0/*
%dir %{_includedir}/mate-vfs-module-2.0
%{_includedir}/mate-vfs-module-2.0/*
%{_libdir}/*.so
%{_libdir}/%{name}-2.0/include
%{_libdir}/pkgconfig/*.pc



%changelog
* Fri Jul 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.0-1
+ Revision: 811346
- new version 1.4.0

* Thu May 31 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.1-1
+ Revision: 801584
- imported package mate-vfs

