%define url_ver %(echo %{version} | cut -d. -f1,2)
%define gstapi 1.0

Summary:	Tool to Manage Flickr Accounts
Name:		frogr
Version:	1.8.1
Release:	1
License:	GPLv3+
Group:		Graphical desktop/GNOME
Url:		https://live.gnome.org/Frogr
Source0:	http://ftp.gnome.org/pub/GNOME/sources/frogr/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libsoup-gnome-2.4)
BuildRequires:	meson

%description
Frogr is a small application for the GNOME desktop that allows users to
manage their accounts in the Flickr image hosting website. It supports
all the basic Flickr features, including uploading pictures, adding
descriptions, setting tags and managing sets and groups pools.

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.%{name}.desktop
%{_datadir}/%{name}/
#{_datadir}/pixmaps/frogr.xpm
%{_datadir}/metainfo/org.gnome.frogr.appdata.xml
%{_iconsdir}/*/*/apps/org.gnome.%{name}*.*
%{_mandir}/man1/frogr.1*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
export CC=gcc
export CXX=g++
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

