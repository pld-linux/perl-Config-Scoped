#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Scoped
Summary:	Config::Scoped - feature rich configuration file parser
Summary(pl.UTF-8):	Config::Scoped - bogaty w możliwości analizator plików konfiguracyjnych
Name:		perl-Config-Scoped
Version:	0.11
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1dce2be606897ea9912f5e19dffe002f
URL:		http://search.cpan.org/dist/Config-Scoped/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Parse-RecDescent
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::Scoped has the following highlights as a configuration file
parser:

- Complex recursive datastructures to any extent with scalars, lists
  and hashes as elements,
- As a subset parses any complex Perl datastructures (no references
  and globs) without do or require,
- Include files with recursion checks,
- Controlled macro expansion in double quoted tokens,
- Lexically scoped parameter assignments and pragma directives,
- Perl quote like constructs to any extent, '', "", and here docs <<,
- Perl code evaluation in Safe compartments,
- Caching and restore with MD5 checks to determine alterations in the
  original config files,
- Standard macro, parameter, declaration redefinition validation, may
  be overridden to validate on semantic knowledge,
- Standard file permission and ownership safety validation, may be
  overridden,
- Fine control for redefiniton warnings with pragma's and other safety
  checks,
- Easy inheritable, may be subclassed to build parsers with
  specialized validation features,
- Condoning syntax checker, semicolons and or commas are not always
  necessary to finish a statement or a list item if the end can be
  guessed by other means like newlines, closing brackets, braces etc.,
- Well spotted messages for syntax errors even within include files
  with correct line numbers and file names,
- Exception based error handling,
- etc.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Config/*.pm
%{perl_vendorlib}/Config/Scoped
%{_mandir}/man3/*
