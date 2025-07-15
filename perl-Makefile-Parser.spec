#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Makefile
%define		pnam	Parser
Summary:	Makefile::Parser - A simple parser for Makefiles
Summary(pl.UTF-8):	Makefile::Parser - prosty analizator plików Makefile
Name:		perl-Makefile-Parser
Version:	0.215
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AG/AGENT/Makefile-Parser-%{version}.tar.gz
# Source0-md5:	f80b65da36c3fd004c8b7067e99c2c9f
Patch0:		%{name}-test.patch
URL:		http://search.cpan.org/dist/Makefile-Parser/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Class-Trigger >= 0.13
BuildRequires:	perl-File-Slurp
BuildRequires:	perl-IPC-Run3 >= 0.036
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Makefile-DOM >= 0.005
%endif
Requires:	perl-Class-Trigger >= 0.13
Requires:	perl-IPC-Run3 >= 0.036
Requires:	perl-Makefile-DOM >= 0.005
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple parser for Makefiles. At this very early stage, the
parser only supports a limited set of features, so it may not
recognize most of the advanced features provided by certain make tools
like GNU make. Its initial purpose is to provide basic support for
another module named Makefile::GraphViz, which is aimed to render the
building process specified by a Makefile using the amazing GraphViz
library.

%description -l pl.UTF-8
Ten pakiet to prosty analizator plików Makefile. Na wstępnym etapie
obsługuje tylko ograniczony zbiór możliwości, więc może nie
rozpoznawać większości zaawansowanych możliwości niektórych
implementacji make, takich jak GNU make. Pierwotnym celem jest
zapewnienie podstawowej obsługi dla innego modułu -
Makefile::GraphViz, którego celem jest renderowanie procesu budowania
opisanego plikiem Makefile przy użyciu biblioteki GraphViz.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%{__sed} -i -e '1s,/usr/bin/env perl,/usr/bin/perl,' script/*

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/makesimple
%attr(755,root,root) %{_bindir}/pgmake-db
%attr(755,root,root) %{_bindir}/plmake
%{perl_vendorlib}/Makefile/AST.pm
%{perl_vendorlib}/Makefile/AST
%{perl_vendorlib}/Makefile/Parser.pm
%{perl_vendorlib}/Makefile/Parser
%{_mandir}/man1/makesimple.1p*
%{_mandir}/man1/pgmake-db.1p*
%{_mandir}/man1/plmake.1p*
%{_mandir}/man3/Makefile::AST*.3pm*
%{_mandir}/man3/Makefile::Parser*.3pm*
