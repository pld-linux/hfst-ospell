Summary:	hfst-ospell library and toy commandline tester
Summary(pl.UTF-8):	Biblioteka hfst-ospell i program testowy
Name:		hfst-ospell
Version:	0.5.2
Release:	1
License:	Apache v2.0
Group:		Applications/Text
#Source0Download: https://github.com/hfst/hfst-ospell/releases
Source0:	https://github.com/hfst/hfst-ospell/archive/v%{version}/hfstospell-%{version}.tar.gz
# Source0-md5:	f625099c311cabe6aa595668e60431ac
Patch0:		%{name}-demos.patch
URL:		http://hfst.github.io/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	libarchive-devel >= 3.0.1
BuildRequires:	libicu-devel >= 4
# -std=c++14
BuildRequires:	libstdc++-devel >= 6:5.0
BuildRequires:	libxml++2-devel >= 2.10.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
Requires:	libxml++2 >= 2.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a minimal hfst optimized lookup format based spell checker
library and a demonstrational implementation of command line based
spell checker.

%description -l pl.UTF-8
Ten pakiet zawiera minimalną bibliotekę do sprawdzania pisowni przy
użyciu zoptymalizowanego wyszukiwania hfst oraz demonstracyjną
implementację działającego z linii poleceń programu do sprawdzania
pisowni.

%package devel
Summary:	Header files for hfst-ospell library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki hfst-ospell
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libarchive-devel >= 3.0.1
Requires:	libicu-devel >= 4
Requires:	libstdc++-devel >= 6:5.0
Requires:	libxml++2-devel >= 2.10.0

%description devel
Header files for hfst-ospell library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki hfst-ospell.

%package static
Summary:	Static hfst-ospell library
Summary(pl.UTF-8):	Statyczna biblioteka hfst-ospell
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hfst-ospell library.

%description static -l pl.UTF-8
Statyczna biblioteka hfst-ospell.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	HFST_TXT2FST=/usr/bin/hfst-txt2fst \
	HFST_FST2FST=/usr/bin/hfst-fst2fst \
	ZIP=/usr/bin/zip \
	--enable-extra-demos \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libhfstospell.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/hfst-ispell
%attr(755,root,root) %{_bindir}/hfst-ospell
%attr(755,root,root) %{_bindir}/hfst-ospell-cicling
%attr(755,root,root) %{_bindir}/hfst-ospell-fsmnlp-2012
%attr(755,root,root) %{_bindir}/hfst-ospell-lrec2013
%attr(755,root,root) %{_bindir}/hfst-ospell-norvig
%attr(755,root,root) %{_bindir}/hfst-ospell-office
%attr(755,root,root) %{_bindir}/hfst-ospell-survey
%attr(755,root,root) %{_libdir}/libhfstospell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhfstospell.so.11
%{_mandir}/man1/hfst-ospell.1*
%{_mandir}/man1/hfst-ospell-office.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhfstospell.so
%{_includedir}/ZHfstOspeller*.h
%{_includedir}/hfst-ol.h
%{_includedir}/hfstol-stdafx.h
%{_includedir}/ol-exceptions.h
%{_includedir}/ospell.h
%{_pkgconfigdir}/hfstospell.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libhfstospell.a
