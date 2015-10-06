#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyzmq
Version  : 14.7.0
Release  : 8
URL      : https://pypi.python.org/packages/source/p/pyzmq/pyzmq-14.7.0.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pyzmq/pyzmq-14.7.0.tar.gz
Summary  : Python bindings for 0MQ
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 HPND LGPL-3.0
Requires: pyzmq-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(libzmq)
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
# PyZMQ: Python bindings for ÃMQ
[![Build Status](https://travis-ci.org/zeromq/pyzmq.svg?branch=master)](https://travis-ci.org/zeromq/pyzmq)

%package python
Summary: python components for the pyzmq package.
Group: Default

%description python
python components for the pyzmq package.


%prep
%setup -q -n pyzmq-14.7.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
