# NOTE: 5.0.0 is the last version supporting python2; for later versions see python3-more_itertools.spec
#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module [see python3-more_itertools.spec instead]

Summary:	More routines for operating on iterables, beyond itertools
Summary(pl.UTF-8):	Uzupełniające itertools dodatkowe funkcje do operowania na zmiennych iterowalnych
Name:		python-more_itertools
Version:	5.0.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/more_itertools/
Source0:	https://files.pythonhosted.org/packages/source/m/more_itertools/more-itertools-%{version}.tar.gz
# Source0-md5:	f2ea58aa336ce6c13b7b225b3bbe305d
URL:		https://github.com/erikrose/more-itertools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-six >= 1.0.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-six >= 1.0.0
%endif
%endif
%if %{with doc}
BuildRequires:	python-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python's itertools library is a gem - you can compose elegant
solutions for a variety of problems with the functions it provides. In
more-itertools we collect additional building blocks, recipes, and
routines for working with Python iterables.

%description -l pl.UTF-8
Biblioteka Pythona itertools to skarb - przy użyciu udostępnianych
funkcji można komponować eleganckie rozwiązania różnych problemów.
W pakiecie more-itertools zebrane są dodatkowe elementy konstrukcyjne,
przepisy i procedury do pracy z pythonowymi zmiennymi iterowalnymi.

%package -n python3-more_itertools
Summary:	More routines for operating on iterables, beyond itertools
Summary(pl.UTF-8):	Uzupełniające itertools dodatkowe funkcje do operowania na zmiennych iterowalnych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-more_itertools
Python's itertools library is a gem - you can compose elegant
solutions for a variety of problems with the functions it provides. In
more-itertools we collect additional building blocks, recipes, and
routines for working with Python iterables.

%description -n python3-more_itertools -l pl.UTF-8
Biblioteka Pythona itertools to skarb - przy użyciu udostępnianych
funkcji można komponować eleganckie rozwiązania różnych problemów.
W pakiecie more-itertools zebrane są dodatkowe elementy konstrukcyjne,
przepisy i procedury do pracy z pythonowymi zmiennymi iterowalnymi.

%package apidocs
Summary:	API documentation for Python more-itertools module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona more-itertools
Group:		Documentation

%description apidocs
API documentation for Python more-itertools module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona more-itertools.

%prep
%setup -q -n more-itertools-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/more_itertools
%{py_sitescriptdir}/more_itertools-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-more_itertools
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/more_itertools
%{py3_sitescriptdir}/more_itertools-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
