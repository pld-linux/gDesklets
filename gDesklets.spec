Summary:	gDesklets - an advanced architecture for desktop applets
Summary(pl):	gDesklets - zaawansowana architektura dla apletów
Name:		gDesklets
Version:	0.12
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/gdesklets/%{name}-%{version}.tar.gz
# Source0-md5:	5a8887fac75599f085f504b1544d624f
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.pycage.de/software_gdesklets.html
BuildRequires:	autoconf
BuildRequires:	automake
Buildrequires:	python >= 2.3
BuildRequires:	python-gnome-devel >= 1.99.14
Buildrequires:	python-pygtk-devel >= 1.99.14
Requires:	python >= 2.3
Requires:	python-gnome >= 1.99.14
Requires:	python-pygtk >= 1.99.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gDesklets provides an advanced architecture for desktop applets.

%description -l pl
gDesklets udostępnia zaawansowaną architekturę dla apletów.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

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

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}/*.pc
%{_datadir}/application-registry/*
%{_datadir}/mime-info/*
%dir %{_datadir}/gdesklets
%attr(755,root,root) %{_datadir}/gdesklets/gdesklets
%{_datadir}/gdesklets/config
%{_datadir}/gdesklets/data
%{_datadir}/gdesklets/desktop
%{_datadir}/gdesklets/display
%{_datadir}/gdesklets/factory
%{_datadir}/gdesklets/locale
%{_datadir}/gdesklets/main
%{_datadir}/gdesklets/sensor
%{_datadir}/gdesklets/utils
%{_datadir}/gdesklets/Sensors
%{_datadir}/gdesklets/Displays
%{_desktopdir}/*
%{_pixmapsdir}/*
