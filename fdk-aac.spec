Name:           fdk-aac
Version:        2.0.0
Release:        3%{?dist}
Summary:        Fraunhofer FDK AAC Codec Library

License:        Apache License V2.0
URL:            https://sourceforge.net/projects/opencore-amr
Source0:        https://github.com/mstorsjo/fdk-aac/archive/v%{version}.tar.gz
BuildRequires:  libtool 
BuildRequires:  gettext
BuildRequires:  autoconf 
BuildRequires:  automake 
BuildRequires:  m4
BuildRequires:	gcc-c++	
BuildRequires:	pkgconfig
BuildRequires:	glibc-devel
BuildRequires:	yasm	


%description
The Fraunhofer FDK AAC Codec Library ("FDK AAC Codec") is software that
implements the MPEG Advanced Audio Coding ("AAC") encoding and decoding
scheme for digital audio.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}


%build

libtoolize
aclocal
automake --add-missing
autoreconf
%configure --enable-shared --disable-static
# make gcc5/gcc6 happy
make CXXFLAGS='%{optflags} -std=c++11 -Wno-narrowing' V=1 %{?_smp_mflags}



%install
make install DESTDIR=$RPM_BUILD_ROOT 
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc ChangeLog NOTICE
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc documentation/*.pdf
%dir %{_includedir}/fdk-aac
%{_includedir}/fdk-aac/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog

* Thu Nov 22 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 2.0.0-3
- Updated to 2.0.0

* Wed Mar 07 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.6-3
- Updated to 0.1.6-3

* Tue Sep 26 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.5-3
- Updated to 0.1.5-3

* Fri Jul 08 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.4-3
- Massive rebuild

* Tue Feb 23 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.4-2
- Rebuilt

* Fri Oct 30 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.4-1
- Initial build
