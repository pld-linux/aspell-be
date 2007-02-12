Summary:	Belarusian dictionary for aspell
Summary(pl.UTF-8):   Białoruski słownik dla aspella
Name:		aspell-be
Version:	0.01
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/be/aspell5-be-%{version}.tar.bz2
# Source0-md5:	61314a1672f98571b32d23486bbd43be
URL:		http://aspell.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Belarusian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Białoruski słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell5-be-%{version}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
