#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-tappy
Version  : 2.2
Release  : 16
URL      : https://github.com/python-tap/tappy/archive/v2.2.tar.gz
Source0  : https://github.com/python-tap/tappy/archive/v2.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: python-tappy-bin
Requires: python-tappy-python3
Requires: python-tappy-python
BuildRequires : Babel
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
tappy
=====
[![PyPI version][pypishield]](https://pypi.python.org/pypi/tap.py)
[![BSD license][license]](https://raw.githubusercontent.com/python-tap/tappy/master/LICENSE)
[![Linux status][travis]](https://travis-ci.org/python-tap/tappy)
[![OS X status][travisosx]](https://travis-ci.org/python-tap/tappy)
[![Windows status][appveyor]](https://ci.appveyor.com/project/mblayman/tappy)
[![Coverage][coverage]](https://codecov.io/github/python-tap/tappy)

%package bin
Summary: bin components for the python-tappy package.
Group: Binaries

%description bin
bin components for the python-tappy package.


%package python
Summary: python components for the python-tappy package.
Group: Default
Requires: python-tappy-python3

%description python
python components for the python-tappy package.


%package python3
Summary: python3 components for the python-tappy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-tappy package.


%prep
%setup -q -n tappy-2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526070196
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tap
/usr/bin/tappy

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
