%define module pydantic-settings
%define uname pydantic_settings

Name:		python-pydantic-settings
Version:	2.8.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pydantic-settings/%{uname}-%{version}.tar.gz
Summary:	Settings management using Pydantic
URL:		https://pypi.org/project/pydantic-settings/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-hatchling
BuildRequires:	python-typing-inspection >= 0.4.0
BuildRequires:	python-pydantic >= 2.7.0
BuildRequires:	python-dotenv >= 0.21.0
Suggests:	python-pyyaml >= 6.0.1
Suggests:	python-tomli >= 2.0.1

%description
Settings management using Pydantic

%prep
%autosetup -p1 -n %{uname}-%{version}

%build
%py_build

%install
%py_install


%files
%{python3_sitelib}/%{uname}-%{version}.dist-info
%{python3_sitelib}/%{uname}/*.py
%{python3_sitelib}/%{uname}/*.typed
%{python3_sitelib}/%{uname}/__pycache__/*.cpython-3*.pyc
%doc README.md
%license LICENSE
