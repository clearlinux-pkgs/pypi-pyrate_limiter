#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v4
# autospec commit: 1ab68ca
#
Name     : pypi-pyrate_limiter
Version  : 3.4.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/9e/df/c5f59ea7557acd6d868f96a6e7faa155994a8ff26e8c325c8daaa48c466f/pyrate_limiter-3.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/9e/df/c5f59ea7557acd6d868f96a6e7faa155994a8ff26e8c325c8daaa48c466f/pyrate_limiter-3.4.0.tar.gz
Summary  : Python Rate-Limiter using Leaky-Bucket Algorithm
Group    : Development/Tools
License  : MIT
Requires: pypi-pyrate_limiter-license = %{version}-%{release}
Requires: pypi-pyrate_limiter-python = %{version}-%{release}
Requires: pypi-pyrate_limiter-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<img align="left" width="95" height="120" src="https://raw.githubusercontent.com/vutran1710/PyrateLimiter/master/docs/_static/logo.png">

%package license
Summary: license components for the pypi-pyrate_limiter package.
Group: Default

%description license
license components for the pypi-pyrate_limiter package.


%package python
Summary: python components for the pypi-pyrate_limiter package.
Group: Default
Requires: pypi-pyrate_limiter-python3 = %{version}-%{release}

%description python
python components for the pypi-pyrate_limiter package.


%package python3
Summary: python3 components for the pypi-pyrate_limiter package.
Group: Default
Requires: python3-core
Provides: pypi(pyrate_limiter)

%description python3
python3 components for the pypi-pyrate_limiter package.


%prep
%setup -q -n pyrate_limiter-3.4.0
cd %{_builddir}/pyrate_limiter-3.4.0
pushd ..
cp -a pyrate_limiter-3.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710182103
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
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

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
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyrate_limiter
cp %{_builddir}/pyrate_limiter-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyrate_limiter/dc6e6fb22a1570634c45a1b4920307f7aa616778 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyrate_limiter/dc6e6fb22a1570634c45a1b4920307f7aa616778

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
