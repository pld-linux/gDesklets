
%include	/usr/lib/rpm/macros.python

Summary:	gDesklets - an advanced architecture for desktop applets
Summary(pl):	gDesklets - zaawansowana architektura dla apletów
Name:		gDesklets
Version:	0.23
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/gdesklets/%{name}-%{version}.tar.bz2
# Source0-md5:	14beb76893e1f7f8f90b8a0b37a6856a
Patch0:		%{name}-install-schemas.patch
URL:		http://gdesklets.gnomedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python >= 2.3
BuildRequires:	python-gnome-devel >= 2.0.0
BuildRequires:	python-pygtk-devel >= 2.0.0
BuildRequires:	swig-python
BuildRequires:	rpm-pythonprov
Requires:	%{name}-display
Requires:	%{name}-sensor
Requires:	python >= 2.3
Requires:	python-gnome >= 2.0.0
Requires:	python-pygtk >= 2.0.0
Requires:	python-gnome-gconf >= 2.0.0
Requires:	python-gnome-ui >= 2.0.0
Requires(post): GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gDesklets provides an advanced architecture for desktop applets.

%description -l pl
gDesklets udostêpnia zaawansowan± architekturê dla apletów.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__automake}
#%%{__autoconf} #disabled because it fuck up everything.... WHY ??? */
%configure \
	--disable-schemas-install
	
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gdesklets/{Sensors,Displays}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{_datadir}/gdesklets
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/gdesklets

find $RPM_BUILD_ROOT%{_datadir}/gdesklets -name "*.py" -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install
                                                                                
%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}/*.pc
%{_datadir}/application-registry/*
%{_datadir}/mime-info/*
%dir %{_datadir}/gdesklets
%attr(755,root,root) %{_datadir}/gdesklets/gdesklets
%dir %{_datadir}/gdesklets/locale
%lang(ar) %{_datadir}/gdesklets/locale/ar
%lang(de) %{_datadir}/gdesklets/locale/de
%lang(es) %{_datadir}/gdesklets/locale/es
%lang(el) %{_datadir}/gdesklets/locale/el
%lang(ko) %{_datadir}/gdesklets/locale/ko
%lang(tr) %{_datadir}/gdesklets/locale/tr
%lang(fr) %{_datadir}/gdesklets/locale/fr
%lang(he) %{_datadir}/gdesklets/locale/he
%lang(nl) %{_datadir}/gdesklets/locale/nl
%lang(pl) %{_datadir}/gdesklets/locale/pl
%lang(pt) %{_datadir}/gdesklets/locale/pt
%lang(sq) %{_datadir}/gdesklets/locale/sq
%lang(sr) %{_datadir}/gdesklets/locale/sr
%lang(sr@Latn) %{_datadir}/gdesklets/locale/sr@Latn
%lang(sv) %{_datadir}/gdesklets/locale/sv
%{_datadir}/gdesklets/config
%{_datadir}/gdesklets/data
%{_datadir}/gdesklets/desktop
%{_datadir}/gdesklets/display
%{_datadir}/gdesklets/factory
%{_datadir}/gdesklets/libdesklets
%{_datadir}/gdesklets/main
%{_datadir}/gdesklets/sensor
%{_datadir}/gdesklets/utils
%{_datadir}/gdesklets/Sensors
%{_datadir}/gdesklets/Displays
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_iconsdir}/gnome/48x48/mimetypes/*.png
%{_mandir}/man1/*
%{_sysconfdir}/gconf/schemas/gdesklets-display-thumbnail.schemas
