%define upstream_name    CPANPLUS-Shell-Default-Plugins-Prereqs
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Plugin for CPANPLUS to automate
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPANPLUS/CPANPLUS-Shell-Default-Plugins-Prereqs-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
#make test

%install
./Build install destdir=%{buildroot}

%clean

%files
%doc  README
%{_mandir}/man3/*
%perl_vendorlib/*



%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 654882
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 401676
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.07-1mdv2010.0
+ Revision: 375959
- import perl-CPANPLUS-Shell-Default-Plugins-Prereqs


* Wed Jan 21 2009 cpan2dist 0.07-1mdv
- initial mdv release, generated with cpan2dist


