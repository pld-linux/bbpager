Summary:	A pager designed for blackbox
Summary(pl):	Pager zaprojektowany dla blackboksa
Name:		bbpager
Version:	0.3.0
Release:	4
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Source0:	http://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-sysconfdir.patch
URL:		http://bbtools.windsofstorm.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
bbpager is like the name suggests: a pager tool for Blackbox.

%description -l pl
bbpager jest tym, co nazwa sugeruje: pagerem dla Blackboksa.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
automake -a -c
%configure
%{__make} CXX="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS BUGS ChangeLog README NEWS TODO data/README.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz data/*.gz
%attr(755,root,root) %{_bindir}/bb*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bbtools/%{name}.*
