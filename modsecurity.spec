#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xF2FC4E45883BCBA4 (Martin.Vierula@trustwave.com)
#
Name     : modsecurity
Version  : 3.0.11
Release  : 8
URL      : https://github.com/SpiderLabs/ModSecurity/releases/download/v3.0.11/modsecurity-v3.0.11.tar.gz
Source0  : https://github.com/SpiderLabs/ModSecurity/releases/download/v3.0.11/modsecurity-v3.0.11.tar.gz
Source1  : https://github.com/SpiderLabs/ModSecurity/releases/download/v3.0.11/modsecurity-v3.0.11.tar.gz.asc
Summary  : ModSecurity API
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: modsecurity-bin = %{version}-%{release}
Requires: modsecurity-lib = %{version}-%{release}
Requires: modsecurity-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : perl
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(lua)
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<img src="https://github.com/SpiderLabs/ModSecurity/raw/v3/master/others/modsec.png" width="50%">

%package bin
Summary: bin components for the modsecurity package.
Group: Binaries
Requires: modsecurity-license = %{version}-%{release}

%description bin
bin components for the modsecurity package.


%package dev
Summary: dev components for the modsecurity package.
Group: Development
Requires: modsecurity-lib = %{version}-%{release}
Requires: modsecurity-bin = %{version}-%{release}
Provides: modsecurity-devel = %{version}-%{release}
Requires: modsecurity = %{version}-%{release}

%description dev
dev components for the modsecurity package.


%package lib
Summary: lib components for the modsecurity package.
Group: Libraries
Requires: modsecurity-license = %{version}-%{release}

%description lib
lib components for the modsecurity package.


%package license
Summary: license components for the modsecurity package.
Group: Default

%description license
license components for the modsecurity package.


%prep
%setup -q -n modsecurity-v3.0.11
cd %{_builddir}/modsecurity-v3.0.11
pushd ..
cp -a modsecurity-v3.0.11 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703617521
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --disable-examples
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%configure --disable-static --disable-examples
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1703617521
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/modsecurity
cp %{_builddir}/modsecurity-v%{version}/LICENSE %{buildroot}/usr/share/package-licenses/modsecurity/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/modsecurity-v%{version}/others/libinjection/COPYING %{buildroot}/usr/share/package-licenses/modsecurity/2f52f7e673436d231eb560ccfc057715bc069c67 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/modsec-rules-check
/usr/bin/modsec-rules-check

%files dev
%defattr(-,root,root,-)
/usr/include/modsecurity/actions/action.h
/usr/include/modsecurity/anchored_set_variable.h
/usr/include/modsecurity/anchored_set_variable_translation_proxy.h
/usr/include/modsecurity/anchored_variable.h
/usr/include/modsecurity/audit_log.h
/usr/include/modsecurity/collection/collection.h
/usr/include/modsecurity/collection/collections.h
/usr/include/modsecurity/debug_log.h
/usr/include/modsecurity/intervention.h
/usr/include/modsecurity/modsecurity.h
/usr/include/modsecurity/rule.h
/usr/include/modsecurity/rule_marker.h
/usr/include/modsecurity/rule_message.h
/usr/include/modsecurity/rule_unconditional.h
/usr/include/modsecurity/rule_with_actions.h
/usr/include/modsecurity/rule_with_operator.h
/usr/include/modsecurity/rules.h
/usr/include/modsecurity/rules_exceptions.h
/usr/include/modsecurity/rules_set.h
/usr/include/modsecurity/rules_set_phases.h
/usr/include/modsecurity/rules_set_properties.h
/usr/include/modsecurity/transaction.h
/usr/include/modsecurity/variable_origin.h
/usr/include/modsecurity/variable_value.h
/usr/lib64/libmodsecurity.so
/usr/lib64/pkgconfig/modsecurity.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libmodsecurity.so.3.0.11
/usr/lib64/libmodsecurity.so.3
/usr/lib64/libmodsecurity.so.3.0.11

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/modsecurity/2f52f7e673436d231eb560ccfc057715bc069c67
/usr/share/package-licenses/modsecurity/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
