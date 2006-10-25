# TODO
# - subpackage for cgi?
# - think and fix the trigger.
#
# Conditional build:
%bcond_with	db3	# build with db3 instead of db 4.x
#
%define		ver		2.01
%define		patchlvl	10
Summary:	The Webalizer - A web server log file analysis thingie
Summary(es):	Software para anАlisis de archivos de log de servidores WWW
Summary(pl):	Webalizer - analizator logСw serwera WWW
Summary(pt_BR):	Um software para anАlise de arquivos de log de servidores WWW
Summary(ru):	Программа анализа log-файла web/ftp/proxy-сервера
Summary(uk):	Програма анал╕зу log-файлу web/ftp/proxy-сервера
Name:		webalizer
Version:	%{ver}_%{patchlvl}
Release:	16.6
License:	GPL v2
Group:		Networking/Utilities
Source0:	ftp://ftp.mrunix.net/pub/webalizer/%{name}-%{ver}-%{patchlvl}-src.tar.bz2
# Source0-md5:	26d0a3c142423678daed2d6f579525d8
Source1:	http://linux.gda.pl/pub/webalizer/%{name}_lang.polish
# Source1-md5:	510bc595699373c4d7a8093a5ea10df3
Source2:	%{name}.sysconfig
Source3:	%{name}.cron
Source4:	%{name}.crontab
Patch0:		%{name}-debian-23.patch
Patch1:		%{name}-nolibnsl.patch
Patch2:		%{name}-conf.patch
Patch3:		%{name}-debian_gcc2_fix.patch
Patch4:		%{name}-largefile.patch
URL:		http://www.mrunix.net/webalizer/
BuildRequires:	autoconf
%{!?with_db3:BuildRequires:	db-devel}
%{?with_db3:BuildRequires:	db3-devel}
BuildRequires:	gd-devel >= 2.0.1
BuildRequires:	gettext-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	zlib-devel
Requires:	%{name}-base = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webdir		/home/services/httpd

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
Webalizer to program analizuj╠cy logi serwera WWW i tworz╠cy strony w
formacie HTML zawieraj╠ce statystyki u©ycia tego© serwera WWW. Wyniki
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

%package base
Summary:	Webalizer programs and manuals
Group:		Networking/Utilities

%description base
Webalizer programs and manual pages.

%prep
%setup -q -n %{name}-%{ver}-%{patchlvl}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

mv -f po/{no,nb}.po
mv -f po/{sr,sr@Latn}.po
mv -f po/{zh,zh_TW}.po

install %{SOURCE1} lang

%build
# don't call aclocal, aclocal.m4 contains only one _local_ macro
%{__autoconf}
CFLAGS="%{rpmcflags} -fsigned-char"
%configure \
	--with-gd=%{_libdir} \
	--with-db \
	--with-dblib \
	--enable-dns
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_webdir}/icons,%{_sysconfdir}/{sysconfig,cron.d,%{name}}}

install sample.conf $RPM_BUILD_ROOT%{_sysconfdir}/webalizer.conf
install webalizer $RPM_BUILD_ROOT%{_bindir}
install webalizer.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo '.so webalizer.1' > $RPM_BUILD_ROOT%{_mandir}/man1/webazolver.1
install msfree.png $RPM_BUILD_ROOT%{_webdir}/icons
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/webalizer
install %{SOURCE3} $RPM_BUILD_ROOT%{_sbindir}/webalizer.cron
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/webalizer
ln -s webalizer $RPM_BUILD_ROOT%{_bindir}/webazolver

for mo in po/*.mo; do
	file=${mo#po/*}
	lang=${file%*.mo}
	install -D $mo $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/webalizer.mo
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- webalizer < 2.01_10-14
echo "Upgrading from webalizer < 2.01_10-14"
chgrp stats %{_sysconfdir}/webalizer/*
chmod g+r %{_sysconfdir}/webalizer/*
for dir in `grep ^OutputDir %{_sysconfdir}/webalizer/*.conf | awk '{ print $2; };'`; do
	if [ -d $dir ]; then
		chown -R stats $dir
	else
		echo "Directory $dir does not exists"
	fi
done

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/webalizer
%attr(2755,root,stats) %dir %{_sysconfdir}/%{name}
%attr(755,root,root) %{_sbindir}/webalizer.cron
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/webalizer

%files base
%defattr(644,root,root,755)
%doc CHANGES *README* country-codes.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/webalizer.conf
%attr(755,root,root) %{_bindir}/webalizer
%attr(755,root,root) %{_bindir}/webazolver
%{_mandir}/man1/*
%{_webdir}/icons/*
