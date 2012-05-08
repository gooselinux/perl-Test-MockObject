Name:           perl-Test-MockObject
Version:        1.09
Release:        6.1%{?dist}
Summary:        Perl extension for emulating troublesome interfaces

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-MockObject/
Source0:        http://www.cpan.org/authors/id/C/CH/CHROMATIC/Test-MockObject-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(CGI)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Pod), perl(Test::Pod::Coverage)
BuildRequires:  perl(UNIVERSAL::can) >= 1.11
BuildRequires:  perl(UNIVERSAL::isa) >= 0.06
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Test::MockObject is a highly polymorphic testing object, capable of
looking like all sorts of objects.  This makes white-box testing much
easier, as you can concentrate on what the code being tested sends to
and receives from the mocked object, instead of worrying about faking
up your own data.  (Another option is not to test difficult things.
Now you have no excuse.)


%prep
%setup -q -n Test-MockObject-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
PERL_RUN_ALL_TESTS=1 ./Build test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*


%changelog
* Mon Aug 30 2010 Mark Chappell <tremble@fedoraproject.org> 1.09-6.1
- EL6 needs the CGI package for the tests to run successfully

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.09-6
- Mass rebuild with perl-5.12.0

* Thu Feb  4 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.09-5
- 552253 merge review

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.09-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.09-1
- update to 1.09

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-2
- rebuild for new perl

* Fri Jun 29 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-1
- Update to 1.08.

* Thu Oct  5 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.07-1
- Update to 1.07.

* Fri Apr 21 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.06-1
- Update to 1.06.

* Tue Apr 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-1
- Update to 1.05.

* Thu Mar 30 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.04-1
- Update to 1.04.
- Makefile.PL -> Build.PL.

* Mon Mar 13 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.03-1
- Update to 1.03.

* Tue Feb 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.02-1
- Update to 1.02.

* Fri Jul 15 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.00-1
- Update to 1.00.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.15-3
- rebuilt

* Tue Dec 28 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.15-2
- Build requires Test::Simple >= 0.44 (bug 2324).

* Wed Dec 01 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.15-0.fdr.1
- Update to 0.15.

* Tue May 25 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.14-0.fdr.1
- Update to 0.14.
- Require perl >= 1:5.6.1 for vendor install dir support.
- Use pure_install to avoid perllocal.pod workarounds.
- Moved make test to section %%check.

* Wed Nov 19 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.12-0.fdr.1
- First build.
