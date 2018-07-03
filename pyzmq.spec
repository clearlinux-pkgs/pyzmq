#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyzmq
Version  : 17.0.0
Release  : 48
URL      : http://pypi.debian.net/pyzmq/pyzmq-17.0.0.tar.gz
Source0  : http://pypi.debian.net/pyzmq/pyzmq-17.0.0.tar.gz
Summary  : Python bindings for 0MQ
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 LGPL-3.0
Requires: pyzmq-python3
Requires: pyzmq-python
Requires: cffi
Requires: py
BuildRequires : Cython
BuildRequires : cffi
BuildRequires : libzmq-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py

BuildRequires : python3-dev
BuildRequires : setuptools

%description
# PyZMQ: Python bindings for ÃMQ
[![Build Status](https://travis-ci.org/zeromq/pyzmq.svg?branch=master)](https://travis-ci.org/zeromq/pyzmq)

%package python
Summary: python components for the pyzmq package.
Group: Default
Requires: pyzmq-python3

%description python
python components for the pyzmq package.


%package python3
Summary: python3 components for the pyzmq package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyzmq package.


%prep
%setup -q -n pyzmq-17.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526833308
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error   -Wl,-z,max-page-size=0x1000 -m64 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
unset LDFLAGS
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
