%define name emma
%define version 0.8
%define release 1
%define prefix /usr
%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Requires: python >= 1.5 , gtk+ >= 1.2.0 , gnome-libs
Summary: Money management program for Gnome/Gtk+
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Distribution: N/A 
Group: Applications/Databases
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: /var/tmp/%{name}-%{version}-%{release}-root
URL: http://rainbow.mimuw.edu.pl/~la181249/
Packager: Lukasz Anforowicz <lanfor@atr.bydgoszcz.pl>
%description
This program allows to easy manage your incomes and expenses.
It is simple in design, but extensible through embeded python
interface. Install it if you want to keep track of your money.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" ./configure --prefix=%{prefix} 
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog README COPYING
%{prefix}/bin/emma
%{prefix}/share/locale/*/*/*
%{prefix}/share/emma/*
%{prefix}/share/gnome/apps/Applications/emma.desktop
%{prefix}/share/gnome/help/emma/*
