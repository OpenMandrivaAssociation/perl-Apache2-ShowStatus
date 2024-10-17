%define upstream_name    Apache2-ShowStatus
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Apache2::ShowStatus - if you want to know what your Apache processes are doing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache2/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	apache-mod_perl
BuildRequires:  apache-mod_perl-devel
BuildRequires:	perl-devel
BuildRequires:	perl(Sys::Proctitle)
BuildRequires:	perl(Apache::Test) >= 1.25
BuildArch:	noarch

%description
This module provides a "PerlInitHandler" that sets the apache's process
title to

 "httpd: ".$r->the_request

The process title is automagically reset when the request is over.

Thus, "top" & Co shows what requests are currently active.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Apache2/ShowStatus.pm
%{_mandir}/*/*

