Summary:	gDesklets - an advanced architecture for desktop applets
Summary(pl):	gDesklets - zaawansowana architektura dla apletów
Name:		gDesklets
Version:	0.30
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/gdesklets/%{name}-%{version}.tar.bz2
# Source0-md5:	20c0d1c4aff84ea29ec777b72319045c
Patch0:		%{name}-am.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-disksize.patch
Patch3:		%{name}-plugin_registry.patch
URL:		http://gdesklets.gnomedesktop.org/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libgtop-devel >= 2.0.0
BuildRequires:	librsvg-devel
BuildRequires:	libtool
BuildRequires:	python >= 2.3
BuildRequires:	python-gnome-devel >= 2.0.0
BuildRequires:	python-pygtk-devel >= 2.0.0
BuildRequires:	swig-python
BuildRequires:	rpm-pythonprov
BuildRequires:	gettext-devel
Requires:	python >= 2.3
Requires:	python-gnome >= 2.0.0
Requires:	python-pygtk-gtk >= 2.0.0
Requires:	python-gnome-bonobo >= 2.0.0
Requires:	python-gnome-bonobo-ui >= 2.0.0
Requires:	python-gnome-gconf >= 2.0.0
Requires:	python-gnome-gtkhtml >= 2.0.0
Requires:	python-gnome-ui >= 2.0.0
Requires(post): GConf2
Requires(post):	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gDesklets provides an advanced architecture for desktop applets.

%description -l pl
gDesklets udostêpnia zaawansowan± architekturê dla apletów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install
	
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gdesklets/{Sensors,Displays}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%py_comp $RPM_BUILD_ROOT%{_datadir}/gdesklets
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/gdesklets

find $RPM_BUILD_ROOT%{_datadir}/gdesklets -name "*.py" -exec rm -f {} \;
rm -f $RPM_BUILD_ROOT%{_datadir}/mime/{XMLnamespaces,globs,magic,application/*}
rm -f $RPM_BUILD_ROOT%{_desktopdir}/mimeinfo.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%gconf_schema_install
update-mime-database %{_datadir}/mime
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}/*.pc
%dir %{_datadir}/gdesklets
%{_datadir}/gdesklets/*.py[co]
%attr(755,root,root) %{_datadir}/gdesklets/gdesklets
%attr(755,root,root) %{_datadir}/gdesklets/gdesklets-daemon
%attr(755,root,root) %{_datadir}/gdesklets/gdesklets-shell
%dir %{_datadir}/gdesklets/locale
%lang(ar) %{_datadir}/gdesklets/locale/ar
%lang(bg) %{_datadir}/gdesklets/locale/bg
%lang(ca) %{_datadir}/gdesklets/locale/ca
%lang(cs) %{_datadir}/gdesklets/locale/cs
%lang(de) %{_datadir}/gdesklets/locale/de
%lang(es) %{_datadir}/gdesklets/locale/es
%lang(el) %{_datadir}/gdesklets/locale/el
%lang(en_CA) %{_datadir}/gdesklets/locale/en_CA
%lang(en_GB) %{_datadir}/gdesklets/locale/en_GB
%lang(eu) %{_datadir}/gdesklets/locale/eu
%lang(hr) %{_datadir}/gdesklets/locale/hr
%lang(hu) %{_datadir}/gdesklets/locale/hu
%lang(is) %{_datadir}/gdesklets/locale/is
%lang(it) %{_datadir}/gdesklets/locale/it
%lang(ja) %{_datadir}/gdesklets/locale/ja
%lang(ko) %{_datadir}/gdesklets/locale/ko
%lang(lt) %{_datadir}/gdesklets/locale/lt
%lang(tr) %{_datadir}/gdesklets/locale/tr
%lang(fr) %{_datadir}/gdesklets/locale/fr
%lang(he) %{_datadir}/gdesklets/locale/he
%lang(nb) %{_datadir}/gdesklets/locale/nb
%lang(nl) %{_datadir}/gdesklets/locale/nl
%lang(pl) %{_datadir}/gdesklets/locale/pl
%lang(pt) %{_datadir}/gdesklets/locale/pt
%lang(pt_BR) %{_datadir}/gdesklets/locale/pt_BR
%lang(ru) %{_datadir}/gdesklets/locale/ru
%lang(sq) %{_datadir}/gdesklets/locale/sq
%lang(sr) %{_datadir}/gdesklets/locale/sr
%lang(sr@Latn) %{_datadir}/gdesklets/locale/sr@Latn
%lang(sv) %{_datadir}/gdesklets/locale/sv
%lang(az) %{_datadir}/gdesklets/locale/az
%lang(ms) %{_datadir}/gdesklets/locale/ms
%{_datadir}/gdesklets/Controls
%{_datadir}/gdesklets/config
%{_datadir}/gdesklets/data
%{_datadir}/gdesklets/display
%{_datadir}/gdesklets/factory
%{_datadir}/gdesklets/libdesklets
%{_datadir}/gdesklets/main
%{_datadir}/gdesklets/plugin
%{_datadir}/gdesklets/scripting
%{_datadir}/gdesklets/sensor
%{_datadir}/gdesklets/shell
%{_datadir}/gdesklets/utils
%{_datadir}/gdesklets/Sensors
%{_datadir}/gdesklets/Displays
%{_datadir}/mime/packages/*.xml
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_iconsdir}/gnome/48x48/mimetypes/*.png
%{_mandir}/man1/*
%{_sysconfdir}/gconf/schemas/*.schemas
