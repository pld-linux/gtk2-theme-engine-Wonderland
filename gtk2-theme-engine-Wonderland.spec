Summary:	Bluecurve theme
Summary(pl):	Motyw Bluecurve
Name:		gtk2-theme-engine-Wonderland
Version:	1.0
Release:	1
License:	GPL
Group:		Themes/Gtk
Source0:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gtk2/GTK2-Wonderland-Engine-%{version}.tar.bz2
# Source0-md5:	0c6a5bbba6ab18984269c7ecbfcebf16
URL:		http://art.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Original Bluecurve engine from Red Hat's artwork package.

%description -l pl
Oryginalny silnik Bluecurve z pakietu grafik Red Hata.

%prep
%setup -q -n Bluecurve

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%dir %{_datadir}/themes/Bluecurve
%{_datadir}/themes/Bluecurve/gtk-2.0
