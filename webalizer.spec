Summary:	The Webalizer - A web server log file analysis thingie
Summary(pl):	Webalizer - analizator logów serwera www
Name:		webalizer
%define		ver	2.01
%define		patchlvl 06
Version:	%{ver}_%{patchlvl}
Release:	3
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://ftp.mrunix.net/pub/webalizer/%{name}-%{ver}-%{patchlvl}-src.tar.bz2
Icon:		webalizer.gif
URL:		http://www.mrunix.net/webalizer/
BuildRequires:	gd-devel >= 2.0.1
BuildRequires:	libpng >= 1.0.8
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	db3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Webalizer is a web server log file analysis program which produces
usage statistics in HTML format for viewing with a browser. The
results are presented in both columnar and graphical format, which
facilitates interpretation. Yearly, monthly, daily and hourly usage
statistics are presented, along with the ability to display usage by
site, URL, referrer, user agent (browser) and country (user agent and
referrer are only available if your web server produces combined log
format files).

%description -l pl
Webalizer to program analizuj±cy logi serwera www i tworz±cy strony w
formacie HTML zawieraj±ce statystyki u¿ycia tego¿ serwera www.

%prep
%setup -q -n %{name}-%{ver}-%{patchlvl}

%build
aclocal
autoconf
CFLAGS="%{rpmcflags} -fsigned-char"
%configure \
	--with-gd \
	--with-db \
	--with-dblib \
	--enable-dns 
#--with-language=polish
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/home/httpd/icons

install sample.conf $RPM_BUILD_ROOT%{_sysconfdir}/webalizer.conf
install webalizer $RPM_BUILD_ROOT%{_bindir}
install webalizer.1 $RPM_BUILD_ROOT%{_mandir}/man1
install msfree.png $RPM_BUILD_ROOT/home/httpd/icons

gzip -9nf CHANGES *README* country-codes.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/webalizer.conf
%attr(755,root,root) %{_bindir}/webalizer
%{_mandir}/man1/*
/home/httpd/icons/*
