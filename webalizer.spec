Summary:	The Webalizer - A web server log file analysis thingie
Summary(es):	Software para anАlisis de archivos de log de servidores WWW.
Summary(pl):	Webalizer - analizator logСw serwera www
Summary(pt_BR):	Um software para anАlise de arquivos de log de servidores WWW
Summary(ru):	Программа анализа log-файла web/ftp/proxy-сервера
Summary(uk):	Програма анал╕зу log-файлу web/ftp/proxy-сервера
Name:		webalizer
%define		ver	2.01
%define		patchlvl 10
Version:	%{ver}_%{patchlvl}
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.mrunix.net/pub/webalizer/%{name}-%{ver}-%{patchlvl}-src.tar.bz2
Patch0:		%{name}-ipv6.patch
Icon:		webalizer.gif
URL:		http://www.mrunix.net/webalizer/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db3-devel
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
Software para anАlisis de archivos de log de servidores WWW.

%description -l pl
Webalizer to program analizuj╠cy logi serwera www i tworz╠cy strony w
formacie HTML zawieraj╠ce statystyki u©ycia tego© serwera www. Wyniki
s╠ prezentowane jednocze╤nie w formacie kolumnowym i graficznym, co
uЁatwia interpretacjЙ. Program prezentuje statystyki roczne,
miesiЙczne, dzienne i godzinowe, ma te© mo©liwo╤Ф wy╤wietlania
statystyk w zale©no╤ci od serwisu, URL-a, strony z ktСrej byЁo
odwoЁanie (czyli nagЁСwka Referer), przegl╠darki i kraju (przy czym
statystyki w zale©no╤ci od przegl╠darki i nagЁСwka Referer s╠ dostЙpne
tylko je╤li serwer loguje informacje o odwiedzinach w formacie
"combined").

%description -l pt_BR
Um analisador de arquivos de log de servidores WWW.

%description -l ru
Webalizer - это программа анализа логов web-сервера, выдающая
статистику в HTML формате, для просмотра броузером. Результаты
представляются как в табличном, так и в графическом формате, что
упрощает интерпретацию. Выдается статистика за год, месяц, день и
почасовая, есть возможность показа статистики по адресу клиента, URL,
ссылкам, браузеру и стране (браузер и ccылки доступны только, если
сервер выдает логи в комбинированном формате).

%description -l uk
Webalizer - це програма анал╕зу лог╕в web-сервера, що вида╓ статистику
в HTML формат╕, для перегляду броузером. Результати подаються як в
табличному, так ╕ в граф╕чному формат╕, що полегшу╓ ╕нтерпретац╕ю.
Вида╓ться статистика за р╕к, м╕сяць, день та погодинна, ╓ можлив╕сть
показу статистики по адрес╕ кл╕╓нта, URL, посиланням, броузеру та
кра╖н╕ (броузер та посилання доступн╕ лише якщо сервер пише логи в
комб╕нованому формат╕).

%prep
%setup -q -n %{name}-%{ver}-%{patchlvl}
%patch0 -p1

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
