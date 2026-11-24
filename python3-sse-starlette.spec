#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	SSE plugin for Starlette
Summary(pl.UTF-8):	Wtyczka SSE dla Starlette
Name:		python3-sse-starlette
Version:	3.7.1
Release:	1
License:	BSD
Group:		Libraries/Python
# PyPI sdist lacks tests/conftest.py and tests/anyio_compat.py
#Source0Download: https://github.com/sysid/sse-starlette/tags
Source0:	https://github.com/sysid/sse-starlette/archive/v%{version}/sse-starlette-%{version}.tar.gz
# Source0-md5:	7f86ffd26859ce16e8512b8198051175
URL:		https://github.com/sysid/sse-starlette
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.11
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-anyio >= 4.7.0
BuildRequires:	python3-asgi-lifespan >= 2.1.0
BuildRequires:	python3-httpx2 >= 2.12.0
BuildRequires:	python3-pytest >= 8.3.4
BuildRequires:	python3-pytest-asyncio >= 0.25.0
BuildRequires:	python3-starlette >= 0.49.1
BuildRequires:	python3-uvicorn >= 0.34.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Server-Sent Events (SSE) plugin for Starlette.

%description -l pl.UTF-8
Wtyczka Server-Sent Events (SSE) dla Starlette.

%prep
%setup -q -n sse-starlette-%{version}

%build
%py3_build_pyproject

%if %{with tests}
# integration and experimentation tests need docker (testcontainers)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=anyio.pytest_plugin,pytest_asyncio.plugin \
%{__python3} -m pytest tests \
	--ignore=tests/integration \
	--ignore=tests/experimentation
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
