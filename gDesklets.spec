Summary:	gDesklets - an advanced architecture for desktop applets
Summary(pl):	gDesklets - zaawansowana architektura dla apletów
Name:		gDesklets
Version:	0.33.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/gdesklets/%{name}-%{version}.tar.bz2
# Source0-md5:	db252b31b56b1c2f49312d5837c311b8
Patch0:		%{name}-am.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-disksize.patch
Patch3:		%{name}-plugin_registry.patch
URL:		http://gdesklets.gnomedesktop.org/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libgtop-devel >= 2.0.0
BuildRequires:	librsvg-devel
BuildRequires:	libtool
BuildRequires:	python >= 1:2.3
BuildRequires:	python-gnome-devel >= 2.0.0
BuildRequires:	python-pygtk-devel >= 2.0.0
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
Requires:	python-gnome >= 2.0.0
Requires:	python-gnome-bonobo >= 2.0.0
Requires:	python-gnome-bonobo-ui >= 2.0.0
Requires:	python-gnome-gconf >= 2.0.0
Requires:	python-gnome-gtkhtml >= 2.0.0
Requires:	python-gnome-ui >= 2.0.0
Requires:	python-pygtk-gtk >= 2.0.0
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
%patch1 -p1 -b .wiget
#%%patch2 -p1
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

%find_lang gdesklets

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%gconf_schema_install
update-mime-database %{_datadir}/mime
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files -f gdesklets.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
#%{_pkgconfigdir}/*.pc
%dir %{_libdir}/gdesklets
%{_libdir}/gdesklets/*.py[co]
%attr(755,root,root) %{_libdir}/gdesklets/gdesklets
%attr(755,root,root) %{_libdir}/gdesklets/gdesklets-daemon
%attr(755,root,root) %{_libdir}/gdesklets/gdesklets-logview
%attr(755,root,root) %{_libdir}/gdesklets/gdesklets-migration-tool
%attr(755,root,root) %{_libdir}/gdesklets/gdesklets-shell

%dir %{_libdir}/gdesklets/Controls
%{_libdir}/gdesklets/Controls/*.py[co]
%dir %{_libdir}/gdesklets/Controls/Calendar
%{_libdir}/gdesklets/Controls/Calendar/*.py[co]
%dir %{_libdir}/gdesklets/Controls/HDDTemp
%{_libdir}/gdesklets/Controls/HDDTemp/*.py[co]
%dir %{_libdir}/gdesklets/Controls/Sensors
%{_libdir}/gdesklets/Controls/Sensors/*.py[co]
%dir %{_libdir}/gdesklets/Controls/System
%{_libdir}/gdesklets/Controls/System/*.py[co]
%dir %{_libdir}/gdesklets/Controls/Time
%{_libdir}/gdesklets/Controls/Time/*.py[co]

%dir %{_libdir}/gdesklets/Sensors
%dir %{_libdir}/gdesklets/Sensors/External
%{_libdir}/gdesklets/Sensors/External/*.py[co]
%dir %{_libdir}/gdesklets/Sensors/FontSelector
%{_libdir}/gdesklets/Sensors/FontSelector/*.py[co]

%dir %{_libdir}/gdesklets/config
%{_libdir}/gdesklets/config/*.py[co]
%dir %{_libdir}/gdesklets/display
%{_libdir}/gdesklets/display/*.py[co]
%dir %{_libdir}/gdesklets/factory
%{_libdir}/gdesklets/factory/*.py[co]

%dir %{_libdir}/gdesklets/libdesklets
%{_libdir}/gdesklets/libdesklets/*.py[co]
%dir %{_libdir}/gdesklets/libdesklets/controls
%{_libdir}/gdesklets/libdesklets/controls/*.py[co]
%dir %{_libdir}/gdesklets/libdesklets/system
%{_libdir}/gdesklets/libdesklets/system/*.py[co]
%attr(755,root,root) %{_libdir}/gdesklets/libdesklets/system/*.so
%dir %{_libdir}/gdesklets/libdesklets/system/FreeBSD
%{_libdir}/gdesklets/libdesklets/system/FreeBSD/*.py[co]
%dir %{_libdir}/gdesklets/libdesklets/system/Linux
%{_libdir}/gdesklets/libdesklets/system/Linux/*.py[co]
%dir %{_libdir}/gdesklets/libdesklets/system/NetBSD
%{_libdir}/gdesklets/libdesklets/system/NetBSD/*.py[co]
%dir %{_libdir}/gdesklets/libdesklets/system/OpenBSD
%{_libdir}/gdesklets/libdesklets/system/OpenBSD/*.py[co]

%dir %{_libdir}/gdesklets/main
%{_libdir}/gdesklets/main/*.py[co]
%dir %{_libdir}/gdesklets/plugin
%{_libdir}/gdesklets/plugin/*.py[co]
%dir %{_libdir}/gdesklets/scripting
%{_libdir}/gdesklets/scripting/*.py[co]
%dir %{_libdir}/gdesklets/sensor
%{_libdir}/gdesklets/sensor/*.py[co]
%dir %{_libdir}/gdesklets/shell
%{_libdir}/gdesklets/shell/*.py[co]
%dir %{_libdir}/gdesklets/shell/plugins
%dir %{_libdir}/gdesklets/shell/plugins/ControlBrowser
%{_libdir}/gdesklets/shell/plugins/ControlBrowser/*.py[co]
%{_libdir}/gdesklets/shell/plugins/ControlBrowser/*.png
%dir %{_libdir}/gdesklets/shell/plugins/ControlCollection
%{_libdir}/gdesklets/shell/plugins/ControlCollection/*.py[co]
%dir %{_libdir}/gdesklets/shell/plugins/ControlsView
%{_libdir}/gdesklets/shell/plugins/ControlsView/*.py[co]
%dir %{_libdir}/gdesklets/shell/plugins/DisplayBrowser
%{_libdir}/gdesklets/shell/plugins/DisplayBrowser/*.py[co]
%{_libdir}/gdesklets/shell/plugins/DisplayBrowser/*.png
%dir %{_libdir}/gdesklets/shell/plugins/DisplayCollection
%{_libdir}/gdesklets/shell/plugins/DisplayCollection/*.py[co]
%dir %{_libdir}/gdesklets/shell/plugins/DisplayView
%{_libdir}/gdesklets/shell/plugins/DisplayView/*.py[co]
%dir %{_libdir}/gdesklets/shell/plugins/Help
%{_libdir}/gdesklets/shell/plugins/Help/*.py[co]
%dir %{_libdir}/gdesklets/shell/plugins/Menu
%{_libdir}/gdesklets/shell/plugins/Menu/*.py[co]
%dir %{_libdir}/gdesklets/shell/plugins/PackageInstaller
%{_libdir}/gdesklets/shell/plugins/PackageInstaller/*.py[co]
%{_libdir}/gdesklets/shell/plugins/PackageInstaller/*.png
%dir %{_libdir}/gdesklets/shell/plugins/Profiles
%{_libdir}/gdesklets/shell/plugins/Profiles/*.py[co]
%dir %{_libdir}/gdesklets/shell/plugins/Shell
%{_libdir}/gdesklets/shell/plugins/Shell/*.py[co]
%dir %{_libdir}/gdesklets/shell/plugins/StatusBar
%{_libdir}/gdesklets/shell/plugins/StatusBar/*.py[co]
%dir %{_libdir}/gdesklets/shell/plugins/ViewSwitch
%{_libdir}/gdesklets/shell/plugins/ViewSwitch/*.py[co]
%dir %{_libdir}/gdesklets/shell/plugins/gDeskletsClient
%{_libdir}/gdesklets/shell/plugins/gDeskletsClient/*.py[co]

%dir %{_libdir}/gdesklets/utils
%{_libdir}/gdesklets/utils/*.py[co]
%attr(755,root,root) %{_libdir}/gdesklets/utils/*.so

%{_libdir}/gdesklets/data
%{_datadir}/mime/packages/*.xml
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_iconsdir}/gnome/48x48/mimetypes/*.png
%{_mandir}/man1/*
%{_sysconfdir}/gconf/schemas/*.schemas
