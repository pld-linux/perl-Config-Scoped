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
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	80d56f8b1ed0e252b5aa9c40b5ad934f
URL:		http://search.cpan.org/dist/Config-Scoped/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Error
BuildRequires:	perl-Parse-RecDescent >= 1.94
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

%description -l pl.UTF-8
Config::Scoped ma następujące cechy jako analizator plików
konfiguracyjnych:
- dowolnie złożone rekurencyjne struktury danych z elementami będącymi
  skalarami, listami i haszami,
- analizowanie dowolnie złożone perlowe struktury danych (bez
  referencji i globów) bez użycia do czy require,
- dołączanie plików ze sprawdzaniem rekurencji,
- kontrolowane rozwijanie makr w tokenach ujętych w cudzysłowy,
- przypisywanie parametrów i obsługa dyrektyw pragma z kontekstem
  leksykalnym,
- obsługa dowolnych perlowych konstrukcji cytowania z użyciem '', "" i
  dokumentów włączanych <<,
- wykonywanie kodu perlowego w segmentach Safe,
- zapamiętywanie (cache) i odtwarzanie z kontrolą MD5 w celu wykrycia
  zmian w oryginalnych plikach konfiguracyjnych,
- kontrola poprawności makr, parametrów i redefinicji deklaracji może
  być przeprowadzana zależnie od wiedzy semantycznej,
- standardowe sprawdzanie uprawnień i własności plików pod kątem
  bezpieczeństwa; może być zmienione,
- dobra kontrola ostrzeżeń o redefinicjach z użyciem dyrektyw pragma,
- łatwe dziedziczenie, można tworzyć podklasy do tworzenia
  analizatorów o wyspecjalizowanym sprawdzaniu poprawności,
- łagodna kontrola składni, średniki i/lub przecinki nie są zawsze
  niezbędne do zakończenia instrukcji czy elementu listy, jeśli koniec
  da się odgadnąć w inny sposób, jak np. z końców linii, nawiasów
  zamykających itp.,
- dobrze wskazujące komunikaty o błędach składni, nawet wewnątrz
  plików dołączanych, z poprawnymi numerami linii i nazwami plików,
- obsługa błędów oparta na wyjątkach,
- itd.

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
