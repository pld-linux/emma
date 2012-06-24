Summary:	Money management program for Gnome/Gtk+
Summary(pl):	Program do zarz�dzania pieni�dzmi
Name:		emma
Version:	0.8
Release:	0.1
License:	GPL
Group:		Applications/Databases
Source0:	http://rainbow.mimuw.edu.pl/~la181249/emma/download-count.php3?get=packages/%{name}-%{version}-1.tar.gz
# Source0-md5:	7dc37a41b9fb2cfc69a3c1a3ac22f102
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-po.patch
URL:		http://rainbow.mimuw.edu.pl/~la181249/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	python-devel >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows to easy manage your incomes and expenses. It is
simple in design, but extensible through embeded python interface.
Install it if you want to keep track of your money.

%description -l pl
Ten program pozwoli Ci �atwo zarz�dza� Twoimi przychodami oraz
wydatkami. Prosty w konstrukcji, ale �atwy w rozbudowie dzi�ki
wbudowanemu interfejsowi j�zyka Python. Zainstaluj Emma je�li chcesz
wiedzie�, gdzie znikaj� Twoje pieni�dze.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	emma_desktopdir=%{_applnkdir}/Utilities

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/emma
%{_datadir}/emma
%{_applnkdir}/Utilities/emma.desktop
