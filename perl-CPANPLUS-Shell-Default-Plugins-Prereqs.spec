
%define realname   CPANPLUS-Shell-Default-Plugins-Prereqs
%define version    0.07
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Plugin for CPANPLUS to automate
Source:     http://www.cpan.org/modules/by-module/CPANPLUS/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(CPANPLUS)
BuildRequires: perl(CPANPLUS::Dist::Build)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

%description
A plugin for CPANPLUS's default shell which will display and/or install any
missing prerequisites for a module. The module can be specified by name, as
a URL or path to the directory of an unpacked module. The plugin assumes
the current directory if no module is specified.





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*


