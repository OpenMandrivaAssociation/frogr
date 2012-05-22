Summary:	Tool to Manage Flickr Accounts
Name:		frogr
Version:	0.7
Release:	1
License:	GPLv3
Group:		Graphical desktop/GNOME
Url:		https://live.gnome.org/Frogr
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)

%description
Frogr is a small application for the GNOME desktop that allows users to
manage their accounts in the Flickr image hosting website. It supports
all the basic Flickr features, including uploading pictures, adding
descriptions, setting tags and managing sets and groups pools.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/pixmaps/frogr.xpm
%{_datadir}/icons/hicolor/*/apps/frogr.*
%{_mandir}/man1/frogr.1*

