#
# Conditional build:
%bcond_with	db3	# build with db3 instead of db 4.x
%bcond_with	lang_pl	# build with --language=polish
#
%define		ver		2.01
%define		patchlvl	10
Summary:	The Webalizer - A web server log file analysis thingie
Summary(es):	Software para an�lisis de archivos de log de servidores WWW
Summary(pl):	Webalizer - analizator log�w serwera www
Summary(pt_BR):	Um software para an�lise de arquivos de log de servidores WWW
Summary(ru):	��������� ������� log-����� web/ftp/proxy-�������
Summary(uk):	�������� ���̦�� log-����� web/ftp/proxy-�������
Name:		webalizer
Version:	%{ver}_%{patchlvl}%{!?lang_pl:pl}
Release:	3
License:	GPL v2
Group:		Networking/Utilities
Source0:	ftp://ftp.mrunix.net/pub/webalizer/%{name}-%{ver}-%{patchlvl}-src.tar.bz2
# Source0-md5:	26d0a3c142423678daed2d6f579525d8
Patch0:		%{name}-ipv6.patch
Patch1:		%{name}-nolibnsl.patch
Icon:		webalizer.gif
URL:		http://www.mrunix.net/webalizer/
BuildRequires:	autoconf
BuildRequires:	automake
%{!?with_db3:BuildRequires:	db-devel}
%{?with_db3:BuildRequires:	db3-devel}
BuildRequires:	gd-devel >= 2.0.1
BuildRequires:	libpng >= 1.0.8
BuildRequires:	zlib-devel
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

%description -l es
Software para an�lisis de archivos de log de servidores WWW.

%description -l pl
Webalizer to program analizuj�cy logi serwera www i tworz�cy strony w
formacie HTML zawieraj�ce statystyki u�ycia tego� serwera www. Wyniki
s� prezentowane jednocze�nie w formacie kolumnowym i graficznym, co
u�atwia interpretacj�. Program prezentuje statystyki roczne,
miesi�czne, dzienne i godzinowe, ma te� mo�liwo�� wy�wietlania
statystyk w zale�no�ci od serwisu, URL-a, strony z kt�rej by�o
odwo�anie (czyli nag��wka Referer), przegl�darki i kraju (przy czym
statystyki w zale�no�ci od przegl�darki i nag��wka Referer s� dost�pne
tylko je�li serwer loguje informacje o odwiedzinach w formacie
"combined").

%description -l pt_BR
Um analisador de arquivos de log de servidores WWW.

%description -l ru
Webalizer - ��� ��������� ������� ����� web-�������, ��������
���������� � HTML �������, ��� ��������� ���������. ����������
�������������� ��� � ���������, ��� � � ����������� �������, ���
�������� �������������. �������� ���������� �� ���, �����, ���� �
���������, ���� ����������� ������ ���������� �� ������ �������, URL,
�������, �������� � ������ (������� � cc���� �������� ������, ����
������ ������ ���� � ��������������� �������).

%description -l uk
Webalizer - �� �������� ���̦�� ��Ǧ� web-�������, �� ����� ����������
� HTML �����Ԧ, ��� ��������� ���������. ���������� ��������� �� �
����������, ��� � � ���Ʀ����� �����Ԧ, �� ������դ ����������æ�.
��������� ���������� �� Ҧ�, ͦ����, ���� �� ���������, � �����צ���
������ ���������� �� ����Ӧ �̦����, URL, ����������, �������� ��
����Φ (������� �� ��������� ������Φ ���� ���� ������ ���� ���� �
���¦�������� �����Ԧ).

%prep
%setup -q -n %{name}-%{ver}-%{patchlvl}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
CFLAGS="%{rpmcflags} -fsigned-char"
%configure \
	--with-gd \
	--with-db \
	--with-dblib \
	--enable-dns \
%if %{with lang_pl}
	--with-language=polish
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/home/services/httpd/icons

install sample.conf $RPM_BUILD_ROOT%{_sysconfdir}/webalizer.conf
install webalizer $RPM_BUILD_ROOT%{_bindir}
install webalizer.1 $RPM_BUILD_ROOT%{_mandir}/man1
install msfree.png $RPM_BUILD_ROOT/home/services/httpd/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES *README* country-codes.txt
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/webalizer.conf
%dir %{_sysconfdir}/%{name}
%attr(755,root,root) %{_bindir}/webalizer
%{_mandir}/man1/*
/home/services/httpd/icons/*
