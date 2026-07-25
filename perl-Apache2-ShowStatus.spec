%define upstream_name    Apache2-ShowStatus
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	Apache2::ShowStatus - if you want to know what your Apache processes are doing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Apache2-ShowStatus
Source0:	https://cpan.metacpan.org/authors/id/O/OP/OPI/Apache2-ShowStatus-%{upstream_version}.tar.gz

BuildRequires:	make
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

