Summary:	A pager designed for blackbox
Summary(pl):	Pager zaprojektowany dla blackboksa
Name:		bbpager
Version:	0.3.0
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-sysconfdir.patch
URL:		http://bbtools.windsofstorm.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
bbpager is like the name suggests: a pager tool for Blackbox.

%description -l pl
bbpager jest tym, co nazwa sugeruje: pagerem dla Blackboksa.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} CXX="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README NEWS TODO data/README.*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bbtools/%{name}.*
%attr(755,root,root) %{_bindir}/bb*
