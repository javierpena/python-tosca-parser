%global pypi_name tosca-parser

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        XXX
Release:        1%{?dist}
Summary:        Parser for TOSCA Simple Profile in YAML

License:        ASL 2.0
URL:            https://github.com/openstack/tosca-parser
Source0:        https://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The TOSCA Parser is an OpenStack project and licensed under Apache 2. 
It is developed to parse TOSCA Simple Profile in YAML. It reads the TOSCA
templates and creates an in-memory graph of TOSCA nodes and their relationship.

%package -n python2-%{pypi_name}
Summary:        Parser for TOSCA Simple Profile in YAML.
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python-pbr >= 1.3
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-babel
BuildRequires:  PyYAML

Requires:       PyYAML
Requires:       python-six
Requires:       python-dateutil

%description -n python2-%{pypi_name}
The TOSCA Parser is an OpenStack project and licensed under Apache 2. 
It is developed to parse TOSCA Simple Profile in YAML. It reads the TOSCA
templates and creates an in-memory graph of TOSCA nodes and their relationship.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Parser for TOSCA Simple Profile in YAML.
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 1.3
BuildRequires:  python3-sphinx
BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3-babel
BuildRequires:  python3-PyYAML

Requires:       python3-PyYAML
Requires:       python3-six
Requires:       python3-dateutil

%description -n python3-%{pypi_name}
The TOSCA Parser is an OpenStack project and licensed under Apache 2. 
It is developed to parse TOSCA Simple Profile in YAML. It reads the TOSCA
templates and creates an in-memory graph of TOSCA nodes and their relationship.
%endif


%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%{__python2} setup.py build

%if 0%{?with_python3}
%{__python3} setup.py build
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%files -n python2-%{pypi_name}
%doc html README.rst
%license LICENSE
%{python2_sitelib}/toscaparser
%{python2_sitelib}/tosca_parser-%{upstream_version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc html README.rst
%license LICENSE
%{python3_sitelib}/toscaparser
%{python3_sitelib}/tosca_parser-%{upstream_version}-py?.?.egg-info

%changelog
