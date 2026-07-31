%define module pydantic-settings
%define oname pydantic_settings

Name:		python-pydantic-settings
Version:	2.14.2
Release:	1
Summary:	Settings management using Pydantic
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/pydantic-settings/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(typing-inspection) >= 0.4.0
BuildRequires:	python%{pyver}dist(pydantic) >= 2.7.0
BuildRequires:	python%{pyver}dist(python-dotenv) >= 0.21.0
Suggests:	python%{pyver}dist(pyyaml) >= 6.0.1
Suggests:	python%{pyver}dist(tomli) >= 2.0.1

%description
Settings management using Pydantic

%files
%doc README.md
%license LICENSE
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
