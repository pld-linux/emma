Summary:	Money management program for Gnome/Gtk+
Summary(pl):	Program do zarz±dzania pieniêdzmi
Name:		emma
Version:	0.8
Release:	0
License:	GPL
Group:		Applications/Databases
Group(de):	Applikationen/Dateibanken
Group(pl):	Aplikacje/Bazy danych
Source0:	http://rainbow.mimuw.edu.pl/~la181249/emma/download-count.php3?get=packages/%{name}-%{version}-1.tar.gz
URL:		http://rainbow.mimuw.edu.pl/~la181249/
BuildRequires:	python-devel >= 1.5
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This program allows to easy manage your incomes and expenses. It is
simple in design, but extensible through embeded python interface.
Install it if you want to keep track of your money.

%description -l pl
Ten program pozwoli Ci ³atwo zarz±dzaæ Twoimi przychodami oraz wydatkami.
Prosty w konstrukcji, ale ³atwy w rozbudowie dziêki wbudowanemu interfejsowi
jêzyka Python. Zainstaluj Emma je¶li chcesz wiedzieæ, gdzie znikaj± Twoje
pieni±dze.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README COPYING
%attr(755,root,root) %{_bindir}/emma
%{_datadir}/locale/*/*/*
%{_datadir}/emma/*
%{_applnkdir}/Applications/emma.desktop
%{_datadir}/gnome/help/emma/*
