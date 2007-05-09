%define real_name Apache2-ShowStatus

Summary:	Apache2::ShowStatus - if you want to know what your Apache processes are doing
Name:		perl-%{real_name}
Version:	0.02
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache2/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Sys::Proctitle)
BuildRequires:	apache-mod_perl
BuildRequires:  apache-mod_perl-devel
BuildRequires:	perl(Apache::Test) >= 1.25
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides a "PerlInitHandler" that sets the apache's process
title to

 "httpd: ".$r->the_request

The process title is automagically reset when the request is over.

Thus, "top" & Co shows what requests are currently active.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Apache2/ShowStatus.pm
%{_mandir}/*/*

