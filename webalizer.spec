%define		ver	1.29
%define		patchlvl 07
Summary:	The Webalizer - A web server log file analysis thingie
Summary(pl):	Webalizer - analizator logów serwera www
Name:		webalizer
Version:	%{ver}_%{patchlvl}
Release:	1
URL:		http://www.mrunix.net/webalizer/
Source:		ftp://ftp.mrunix.net/pub/webalizer/pre-release/%{name}-%{ver}-%{patchlvl}-src.tar.bz2
Vendor:		Bradford L. Barrett <brad@mrunix.net>
Copyright:	GPL
Group:		Networking/Utilities
Group(pl):	Sieæ/U¿ytki
#Icon:		webalizer.gif
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
Webalizer to program analizuj±cy logi serwera www i tworz±cy strony
w formacie HTML zawieraj±ce statystyki u¿ycia tego¿ serwera www.

%prep
%setup -q -n %{name}-%{ver}-%{patchlvl}

%build
%configure --with-gd 
#--with-language=polish
make CFLAGS="$RPM_OPT_FLAGS -fsigned-char"  

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m644 sample.conf $RPM_BUILD_ROOT/etc/webalizer.conf
install -m755 -s webalizer $RPM_BUILD_ROOT%{_bindir}
install -m644 webalizer.1 $RPM_BUILD_ROOT%{_mandir}/man1/webalizer.1
gzip -9nf CHANGES README country-codes.txt $RPM_BUILD_ROOT%{_mandir}/man1/webalizer.1

install -d $RPM_BUILD_ROOT/home/httpd/html/usage
install -m644 msfree.gif $RPM_BUILD_ROOT/home/httpd/html/usage

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz README.gz country-codes.txt.gz
%config(noreplace) /etc/webalizer.conf
%attr(755,root,root) %{_bindir}/webalizer
%{_mandir}/man1/webalizer.1.gz
%dir /home/httpd/html/usage
/home/httpd/html/usage/msfree.gif

%changelog
* Tue May 25 1999 Arkadiusz Mi¶kiewicz <misiek@pld.org.pl>
  [1.22-03]
- new version

* Fri Jan 08 1999 Simon Liddington <sjl96v@ecs.soton.ac.uk>
  [1.20-11]
  Installs manpage
  Config file installed as config

* Mon Jul 27 1998 Arne Coucheron <arneco@online.no>
  [1.20-07]

* Sun Jul 26 1998 Arne Coucheron <arneco@online.no>
  [1.12-10]

* Sun Jun 14 1998 Arne Coucheron <arneco@online.no>
  [1.12-09]

* Sun Jun 07 1998 Arne Coucheron <arneco@online.no>
  [1.12-08]

* Fri Jun 05 1998 Arne Coucheron <arneco@online.no>
  [1.00-05]

* Wed May 27 1998 Arne Coucheron <arneco@online.no>
  [1.00-04]
- using predefined %%{name} and %%{version} macros
- using %defattr macro in file list, this requires rpm 2.5 to build
- installing msfree.gif to /home/httpd/html/usage
- added -q parameter to %setup
- added CHANGES and TODO to %doc

* Fri May 08 1998 Arne Coucheron <arneco@online.no>
  [0.99.06-1]

* Sat Jan 31 1998 Arne Coucheron <arneco@online.no>
- First release
