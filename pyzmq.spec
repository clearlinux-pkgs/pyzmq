#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyzmq
Version  : 19.0.2
Release  : 68
URL      : https://files.pythonhosted.org/packages/05/77/7483975d84fe1fd24cc67881ba7810e0e7b3ee6c2a0e002a5d6703cca49b/pyzmq-19.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/05/77/7483975d84fe1fd24cc67881ba7810e0e7b3ee6c2a0e002a5d6703cca49b/pyzmq-19.0.2.tar.gz
Summary  : Python bindings for 0MQ
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 LGPL-3.0
Requires: pyzmq-license = %{version}-%{release}
Requires: pyzmq-python = %{version}-%{release}
Requires: pyzmq-python3 = %{version}-%{release}
Requires: cffi
Requires: py
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : libzmq-dev
BuildRequires : py
BuildRequires : python3-dev

%description
# PyZMQ: Python bindings for ØMQ
[![Build Status](https://travis-ci.org/zeromq/pyzmq.svg?branch=master)](https://travis-ci.org/zeromq/pyzmq)

%package license
Summary: license components for the pyzmq package.
Group: Default

%description license
license components for the pyzmq package.


%package python
Summary: python components for the pyzmq package.
Group: Default
Requires: pyzmq-python3 = %{version}-%{release}

%description python
python components for the pyzmq package.


%package python3
Summary: python3 components for the pyzmq package.
Group: Default
Requires: python3-core
Provides: pypi(pyzmq)

%description python3
python3 components for the pyzmq package.


%prep
%setup -q -n pyzmq-19.0.2
cd %{_builddir}/pyzmq-19.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1596207274
export GCC_IGNORE_WERROR=1
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export FCFLAGS=$FFLAGS
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyzmq
cp %{_builddir}/pyzmq-19.0.2/COPYING.BSD %{buildroot}/usr/share/package-licenses/pyzmq/7a2caf1ffc9ec4ace81dc6d16dd1bfdf800036b8
cp %{_builddir}/pyzmq-19.0.2/COPYING.LESSER %{buildroot}/usr/share/package-licenses/pyzmq/712937582a8adeb3928fed8f08ef6a6dbcf68667
cp %{_builddir}/pyzmq-19.0.2/bundled/zeromq/COPYING %{buildroot}/usr/share/package-licenses/pyzmq/99b1a5c7351fd39a26db3b560ce91eec4a3aca3d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyzmq/712937582a8adeb3928fed8f08ef6a6dbcf68667
/usr/share/package-licenses/pyzmq/7a2caf1ffc9ec4ace81dc6d16dd1bfdf800036b8
/usr/share/package-licenses/pyzmq/99b1a5c7351fd39a26db3b560ce91eec4a3aca3d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
