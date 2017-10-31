#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyzmq
Version  : 16.0.3
Release  : 33
URL      : http://pypi.debian.net/pyzmq/pyzmq-16.0.3.tar.gz
Source0  : http://pypi.debian.net/pyzmq/pyzmq-16.0.3.tar.gz
Summary  : Python bindings for 0MQ
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 LGPL-3.0
Requires: pyzmq-legacypython
Requires: pyzmq-python3
Requires: pyzmq-python
Requires: cffi
Requires: py
BuildRequires : Cython
BuildRequires : cffi
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# PyZMQ: Python bindings for ÃMQ
[![Build Status](https://travis-ci.org/zeromq/pyzmq.svg?branch=master)](https://travis-ci.org/zeromq/pyzmq)

%package dev
Summary: dev components for the pyzmq package.
Group: Development
Provides: pyzmq-devel

%description dev
dev components for the pyzmq package.


%package legacypython
Summary: legacypython components for the pyzmq package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pyzmq package.


%package python
Summary: python components for the pyzmq package.
Group: Default
Requires: pyzmq-legacypython
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
%setup -q -n pyzmq-16.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1509460125
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1509460125
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib/python2.7/site-packages/zmq/include/zmq.h
/usr/lib/python2.7/site-packages/zmq/include/zmq_utils.h
/usr/lib/python3.6/site-packages/zmq/include/zmq.h
/usr/lib/python3.6/site-packages/zmq/include/zmq_utils.h

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
