Summary:	A pager designed for blackbox
Summary(pl):	Pager zaprojektowany dla blackboksa
Name:		bbpager
Version:	0.3.0
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
URL:		http://bbtools.windsofstorm.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
bbpager is like the name suggests: a pager tool for Blackbox. For now
it uses KDE wm-hints to get the information from Blackbox. So if you
want to use it be sure to enable KDE support. This means you have to
configure it with: ./configure --enable-kde.

%description -l pl
bbpager jest tym, co nazwa sugeruje: pagerem dla Blackboksa. Mo¿e
u¿ywaæ KDE wm-hints do pobierania informacji od Blackboksa. Aby
w³±czyæ wsparcie dla KDE, musi byæ skompilowany z ./configure
--enable-kde.

%prep
%setup -q
%build
aclocal
autoconf
automake -a -c
%configure
%{__make} CXX="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README NEWS TODO data/README.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz data/*.gz
%attr(755,root,root) %{_bindir}/bbpager
%config %{_datadir}/bbtools/bbpager.*
