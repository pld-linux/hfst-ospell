Summary:	hfst-ospell library and toy commandline tester
Summary(pl.UTF-8):	Biblioteka hfst-ospell i program testowy
Name:		hfst-ospell
Version:	0.1.1
Release:	1
License:	Apache v2.0
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/hfst/%{name}-%{version}.tar.gz
# Source0-md5:	98ce8831bf70a604c7d217369bb36572
URL:		http://hfst.sourceforge.net/
BuildRequires:	libstdc++-devel
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
Requires:	libstdc++-devel

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

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/hfst-ospell
%attr(755,root,root) %{_libdir}/libhfstospell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhfstospell.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhfstospell.so
%{_libdir}/libhfstospell.la
%{_includedir}/hfst-ol.h
%{_includedir}/ospell.h
%{_pkgconfigdir}/hfstospell.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libhfstospell.a
