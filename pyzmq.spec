#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyzmq
Version  : 17.1.2
Release  : 52
URL      : https://files.pythonhosted.org/packages/b9/6a/bc9277b78f5c3236e36b8c16f4d2701a7fd4fa2eb697159d3e0a3a991573/pyzmq-17.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/6a/bc9277b78f5c3236e36b8c16f4d2701a7fd4fa2eb697159d3e0a3a991573/pyzmq-17.1.2.tar.gz
Summary  : Python bindings for 0MQ
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 LGPL-3.0
Requires: pyzmq-python3
Requires: pyzmq-license
Requires: pyzmq-python
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
%setup -q -n pyzmq-17.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533909672
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error   -Wl,-z,max-page-size=0x1000 -m64 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
unset LDFLAGS
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pyzmq
cp COPYING.BSD %{buildroot}/usr/share/doc/pyzmq/COPYING.BSD
cp COPYING.LESSER %{buildroot}/usr/share/doc/pyzmq/COPYING.LESSER
cp bundled/zeromq/COPYING %{buildroot}/usr/share/doc/pyzmq/bundled_zeromq_COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/pyzmq/COPYING.BSD
/usr/share/doc/pyzmq/COPYING.LESSER
/usr/share/doc/pyzmq/bundled_zeromq_COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
