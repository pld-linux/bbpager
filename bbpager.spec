Summary:	A pager designed for blackbox
Name:		bbpager
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
URL:		http://bbtools.windsofstorm.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
bbpager is like the name suggests: a pager tool for Blackbox. For now
it uses KDE wm-hints to get the information from Blackbox. So if you
want to use it be sure to enable KDE support. This means you have to
configure it with: ./configure --enable-kde.


%prep
%setup -q
%build
aclocal
autoconf
automake -a -c
%configure
%{__make}

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
