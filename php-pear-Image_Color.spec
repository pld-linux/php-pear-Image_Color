%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Color
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Manage and handles color data and conversions
Summary(pl):	%{_pearname} - obs�uga konwersji i zarz�dzania kolorami
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fdf3699039d3e1557ad479a6bc9b84cc
URL:		http://pear.php.net/package/Image_Color/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-gd
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manage and handles color data and conversions.

In PEAR status of this package is: %{_status}.

%description -l pl
Zarz�dzanie i obs�uga danych o kolorach i ich konwersji.

Ta klasa ma w PEAR status: %{_status}.

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
