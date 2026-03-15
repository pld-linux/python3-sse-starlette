#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	sse_starlette
Summary:	SSE plugin for Starlette
Summary(pl.UTF-8):	Wtyczka SSE dla Starlette
Name:		python3-sse-starlette
Version:	3.3.2
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sse-starlette/
Source0:	https://files.pythonhosted.org/packages/source/s/sse-starlette/%{module}-%{version}.tar.gz
# Source0-md5:	0cf7ee12666fd79aaeaee1ecfed25cef
URL:		https://github.com/sysid/sse-starlette
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-anyio >= 4.7.0
BuildRequires:	python3-pytest
BuildRequires:	python3-starlette >= 0.49.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-anyio >= 4.7.0
Requires:	python3-starlette >= 0.49.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Server-Sent Events (SSE) plugin for Starlette.

%description -l pl.UTF-8
Wtyczka Server-Sent Events (SSE) dla Starlette.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/sse_starlette
%{py3_sitescriptdir}/sse_starlette-%{version}.dist-info
