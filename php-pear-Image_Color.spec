%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Color
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Manage and handles color data and conversions
Summary(pl):	%{_pearname} - obs³uga konwersji i zarz±dzania kolorami
Name:		php-pear-%{_pearname}
Version:	0.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	d7603bc16992e2dae9f104e4ccab6240
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-gd
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manage and handles color data and conversions.

This class has in PEAR status: %{_status}

%description -l pl
Zarz±dzanie i obs³uga danych o kolorach i ich konwersji.

Ta klasa ma w PEAR status: %{_status}

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
