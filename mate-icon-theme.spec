Summary:	Default icon theme for MATE enviroment
Name:		mate-icon-theme
Version:	1.6.3
Release:	1
License:	GPL
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	0cb55a9676723225227cd679be19461e
BuildRequires:	gtk+
BuildRequires:	icon-naming-utils
BuildRequires:	intltool
BuildArch:	noarch
Provides:	xdg-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkgconfigdir	%{_datadir}/pkgconfig

%description
Default icon theme for MATE enviroment.

%package devel
Summary:	Pkgconfig file
Group:		Development

%description devel
MATE icon theme pkgconfig file.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_iconsdir}/{mate,menta}/*/places/inode-directory.*

gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/mate
gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/menta

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%{_iconsdir}/mate
%{_iconsdir}/menta

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc

