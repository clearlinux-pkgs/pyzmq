#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyzmq
Version  : 18.0.0
Release  : 54
URL      : https://files.pythonhosted.org/packages/64/8d/78975da77627fd863c08e8ea3c7cebce7e51bed2936be5118de6b0050638/pyzmq-18.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/64/8d/78975da77627fd863c08e8ea3c7cebce7e51bed2936be5118de6b0050638/pyzmq-18.0.0.tar.gz
Summary  : Python bindings for 0MQ
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 LGPL-3.0
Requires: pyzmq-license = %{version}-%{release}
Requires: pyzmq-python = %{version}-%{release}
Requires: pyzmq-python3 = %{version}-%{release}
Requires: cffi
Requires: gevent
Requires: py
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : libzmq-dev
BuildRequires : py
BuildRequires : python3-dev

%description
# PyZMQ: Python bindings for ÃMQ
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

%description python3
python3 components for the pyzmq package.


%prep
%setup -q -n pyzmq-18.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550596660
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
unset LDFLAGS
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyzmq
cp COPYING.BSD %{buildroot}/usr/share/package-licenses/pyzmq/COPYING.BSD
cp COPYING.LESSER %{buildroot}/usr/share/package-licenses/pyzmq/COPYING.LESSER
cp bundled/zeromq/COPYING %{buildroot}/usr/share/package-licenses/pyzmq/bundled_zeromq_COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyzmq/COPYING.BSD
/usr/share/package-licenses/pyzmq/COPYING.LESSER
/usr/share/package-licenses/pyzmq/bundled_zeromq_COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
