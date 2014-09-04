Name:           persistence-common-object
Version:        1.0.1
Release:        0
Summary:        GENIVI Persistence Common Object (PCO) library
License:	MPL-2.0
Group:		Automotive/GENIVI
Url:            http://git.projects.genivi.org/?p=persistence/persistence-common-object.git;a=summary
Source0:        %name-%version.tar.xz
Source1001: 	persistence-common-object.manifest
BuildRequires:	autoconf >= 2.64, automake >= 1.11
BuildRequires:  libtool >= 2.2
BuildRequires:  pkgconfig
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(automotive-dlt)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(dbus-1)


%description
This library provides a low level persistent key/value store mechanism
intended to be used by GENIVI components.

%package devel
Summary:  Development files for package %{name}
Group:    Automotive/GENIVI
Requires: %{name} = %{version}
Requires: pkgconfig(zlib)
%description devel
This package provides header files and other developer related files
for package %{name}.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen --disable-static --with-database=key-value-store

make %{?_smp_mflags}

%install
%make_install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_libdir}/libpers_common.so.*
%config %{_sysconfdir}/dbus-1/system.d/org.genivi.persistence.admin.conf
%{_datadir}/dbus-1/interfaces/org.genivi.persistence.admin.xml

%files devel
%manifest %{name}.manifest
%{_includedir}/*.h
%{_libdir}/libpers_common.so
%{_libdir}/pkgconfig/libperscommon.pc

%changelog
