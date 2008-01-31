%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Color
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Manage and handles color data and conversions
Summary(pl.UTF-8):	%{_pearname} - obsługa konwersji i zarządzania kolorami
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a4a1a6f5c0f72d235930902cc1ee2e94
URL:		http://pear.php.net/package/Image_Color/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(gd)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manage and handles color data and conversions.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Zarządzanie i obsługa danych o kolorach i ich konwersji.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
