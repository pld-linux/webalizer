# TODO
# - subpackage for cgi?
# - move icons out of /home/services
# - think and fix the trigger.
# - create workaround for language selection
#
# Conditional build:
%bcond_with	db3	# build with db3 instead of db 4.x
#
%define		ver		2.23
%define		patchlvl	08
Summary:	The Webalizer - A web server log file analysis thingie
Summary(es.UTF-8):	Software para análisis de archivos de log de servidores WWW
Summary(pl.UTF-8):	Webalizer - analizator logów serwera WWW
Summary(pt_BR.UTF-8):	Um software para análise de arquivos de log de servidores WWW
Summary(ru.UTF-8):	Программа анализа log-файла web/ftp/proxy-сервера
Summary(uk.UTF-8):	Програма аналізу log-файлу web/ftp/proxy-сервера
Name:		webalizer
Version:	%{ver}_%{patchlvl}
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	ftp://ftp.mrunix.net/pub/webalizer/%{name}-%{ver}-%{patchlvl}-src.tar.bz2
# Source0-md5:	d25a9715dcbfe67ddf86816c27fbda2b

Source2:	%{name}.sysconfig
Source3:	%{name}.cron
Source4:	%{name}.crontab
#
Patch100:	01_symlink_vulnerability.diff
Patch101:	02_fix_a_spelling_error.diff
Patch102:	03_fix_etc_path_in_man.diff
Patch103:	04_Fix_cast_warnings_in_output.c.diff
Patch104:	05_apache_logio.diff
Patch105:	06_apache_logio_optional.diff
Patch106:	07_apache_logio_color_config.diff
Patch107:	08_use_memmove_for_overlapping_blocks.diff
Patch108:	14_add_search_engines.diff
Patch109:	15_ignore_localhost.diff
Patch110:	17_fix_typo_supress_suppress_in_sample.conf.diff
Patch111:	18_ttf_support_throught_libgd.diff
Patch112:	22_php_as_htm_in_sample.conf.diff
Patch113:	23_gettext_first_part.diff
Patch114:	24_gettext_generated.diff
Patch115:	25_add_convertlang2po.diff
Patch116:	26_gettext_po_files.diff
#
Patch0:		%{name}-nolibnsl.patch
Patch1:		%{name}-conf.patch
URL:		http://www.mrunix.net/webalizer/
BuildRequires:	autoconf
%{!?with_db3:BuildRequires:	db-devel}
%{?with_db3:BuildRequires:	db3-devel}
BuildRequires:	gd-devel >= 2.0.1
BuildRequires:	gettext-tools
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	zlib-devel
Requires:	%{name}-base = %{version}-%{release}
Requires:	crondaemon
# sr@Latn vs. sr@latin
#Conflicts:	glibc-misc < 6:2.7
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

%description -l es.UTF-8
Software para análisis de archivos de log de servidores WWW.

%description -l pl.UTF-8
Webalizer to program analizujący logi serwera WWW i tworzący strony w
formacie HTML zawierające statystyki użycia tegoż serwera WWW. Wyniki
są prezentowane jednocześnie w formacie kolumnowym i graficznym, co
ułatwia interpretację. Program prezentuje statystyki roczne,
miesięczne, dzienne i godzinowe, ma też możliwość wyświetlania
statystyk w zależności od serwisu, URL-a, strony z której było
odwołanie (czyli nagłówka Referer), przeglądarki i kraju (przy czym
statystyki w zależności od przeglądarki i nagłówka Referer są dostępne
tylko jeśli serwer loguje informacje o odwiedzinach w formacie
"combined").

%description -l pt_BR.UTF-8
Um analisador de arquivos de log de servidores WWW.

%description -l ru.UTF-8
Webalizer - это программа анализа логов web-сервера, выдающая
статистику в HTML формате, для просмотра броузером. Результаты
представляются как в табличном, так и в графическом формате, что
упрощает интерпретацию. Выдается статистика за год, месяц, день и
почасовая, есть возможность показа статистики по адресу клиента, URL,
ссылкам, браузеру и стране (браузер и ccылки доступны только, если
сервер выдает логи в комбинированном формате).

%description -l uk.UTF-8
Webalizer - це програма аналізу логів web-сервера, що видає статистику
в HTML форматі, для перегляду броузером. Результати подаються як в
табличному, так і в графічному форматі, що полегшує інтерпретацію.
Видається статистика за рік, місяць, день та погодинна, є можливість
показу статистики по адресі клієнта, URL, посиланням, броузеру та
країні (броузер та посилання доступні лише якщо сервер пише логи в
комбінованому форматі).

%package base
Summary:	Webalizer programs and manuals
Summary(pl.UTF-8):	Webalizer i dokumentacja do niego
Group:		Networking/Utilities

%description base
Webalizer programs and manual pages.

%description base -l pl.UTF-8
Webalizer i dokumentacja do niego.

%prep
%setup -q -n %{name}-%{ver}-%{patchlvl}
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1

%patch0 -p1
%patch1 -p1

mv -f po/{no,nb}.po
mv -f po/{sr,sr@latin}.po
mv -f po/{zh,zh_TW}.po

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

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/webalizer
%attr(2755,root,stats) %dir %{_sysconfdir}/%{name}
%attr(755,root,root) %{_sbindir}/webalizer.cron
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/webalizer

%files base -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES *README* country-codes.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/webalizer.conf
%attr(755,root,root) %{_bindir}/webalizer
%attr(755,root,root) %{_bindir}/webazolver
%{_mandir}/man1/*
%dir %{_webdir}
%dir %{_webdir}/icons
%{_webdir}/icons/*
