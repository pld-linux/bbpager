Summary:	A pager designed for blackbox
Summary(pl):	Pager zaprojektowany dla blackboksa
Name:		bbpager
Version:	0.3.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
# Source0-md5:	27e575bd87be25e2fe8a116412d933cc
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
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README NEWS TODO data/README.*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bbtools/%{name}.*
%attr(755,root,root) %{_bindir}/bb*
