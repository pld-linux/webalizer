%define		ver	1.31
%define		patchlvl 06
Summary:	The Webalizer - A web server log file analysis thingie
Summary(pl):	Webalizer - analizator logów serwera www
Name:		webalizer
Version:	%{ver}_%{patchlvl}
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source:		ftp://ftp.mrunix.net/pub/webalizer/pre-release/%{name}-%{ver}-%{patchlvl}-src.tgz
Patch:		webalizer-shared_gd.patch
Icon:		webalizer.gif
URL:		http://www.mrunix.net/webalizer/
BuildRequires:	gd-devel >= 1.6.2
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The Webalizer is a web server log file analysis program which produces
usage statistics in HTML format for viewing with a browser.  The results
are presented in both columnar and graphical format, which facilitates
interpretation.  Yearly, monthly, daily and hourly usage statistics are
presented, along with the ability to display usage by site, URL, referrer,
user agent (browser) and country (user agent and referrer are only
available if your web server produces combined log format files).

%description -l pl
Webalizer to program analizuj±cy logi serwera www i tworz±cy strony w
formacie HTML zawieraj±ce statystyki u¿ycia tego¿ serwera www.

%prep
%setup -q -n %{name}-%{ver}-%{patchlvl}
%patch -p1

%build
aclocal
autoconf
%configure --with-gd
#--with-language=polish
make CFLAGS="$RPM_OPT_FLAGS -fsigned-char"  

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/home/httpd/html/usage

install sample.conf $RPM_BUILD_ROOT%{_sysconfdir}/webalizer.conf
install -s webalizer $RPM_BUILD_ROOT%{_bindir}
install webalizer.1 $RPM_BUILD_ROOT%{_mandir}/man1/webalizer.1
install msfree.png $RPM_BUILD_ROOT/home/httpd/html/usage

gzip -9nf CHANGES README country-codes.txt \
	$RPM_BUILD_ROOT%{_mandir}/man1/webalizer.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config(noreplace) %{_sysconfdir}/webalizer.conf
%attr(755,root,root) %{_bindir}/webalizer
%{_mandir}/man1/*
/home/httpd/html/usage
