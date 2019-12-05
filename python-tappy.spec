#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-tappy
Version  : 2.6.2
Release  : 30
URL      : https://github.com/python-tap/tappy/archive/v2.6.2/tappy-2.6.2.tar.gz
Source0  : https://github.com/python-tap/tappy/archive/v2.6.2/tappy-2.6.2.tar.gz
Summary  : Test Anything Protocol (TAP) tools for Python
Group    : Development/Tools
License  : BSD-2-Clause
Requires: python-tappy-bin = %{version}-%{release}
Requires: python-tappy-license = %{version}-%{release}
Requires: python-tappy-python = %{version}-%{release}
Requires: python-tappy-python3 = %{version}-%{release}
BuildRequires : Babel
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : tox
BuildRequires : util-linux
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
Requires: python-tappy-license = %{version}-%{release}

%description bin
bin components for the python-tappy package.


%package license
Summary: license components for the python-tappy package.
Group: Default

%description license
license components for the python-tappy package.


%package python
Summary: python components for the python-tappy package.
Group: Default
Requires: python-tappy-python3 = %{version}-%{release}

%description python
python components for the python-tappy package.


%package python3
Summary: python3 components for the python-tappy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-tappy package.


%prep
%setup -q -n tappy-2.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571844850
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-tappy
cp %{_builddir}/tappy-2.6.2/LICENSE %{buildroot}/usr/share/package-licenses/python-tappy/d0693ae3fe545a42770e2e03087f9ebdde726bb4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tap
/usr/bin/tappy

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-tappy/d0693ae3fe545a42770e2e03087f9ebdde726bb4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
