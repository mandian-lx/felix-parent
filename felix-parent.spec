%{?_javapackages_macros:%_javapackages_macros}

Name:           felix-parent
Version:        2.1
Release:        13.1
Summary:        Parent POM file for Apache Felix Specs
License:        ASL 2.0
Group:          Development/Java
URL:            http://felix.apache.org/
Source0:        http://repo1.maven.org/maven2/org/apache/felix/felix-parent/%{version}/%{name}-%{version}-source-release.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.mockito:mockito-all)

# FIXME auto-requires are not generated
Requires: easymock
Requires: mockito

%description
Parent POM file for Apache Felix Specs.

%prep
%setup -q -n felix-parent-%{version}
%mvn_alias : :felix
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin org.codehaus.mojo:ianal-maven-plugin
%pom_remove_plugin :apache-rat-plugin

# wagon ssh dependency unneeded
%pom_xpath_remove pom:extensions

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Thu Feb 23 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-13
- Regenerate build-requires

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Michael Simacek <msimacek@redhat.com> - 2.1-11
- Remove BR on site-plugin and release-plugin

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-10
- Add missing requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Michael Simacek <msimacek@redhat.com> - 2.1-7
- Add BR maven-release-plugin

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-5
- Rebuild to regenerate Maven auto-requires

* Wed Mar 05 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-4
- Remove build extensions from pom

* Mon Aug 5 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.1-3
- Remove apache-rat-plugin.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Alexander Kurtakov <akurtako@redhat.com> 2.1-1
- Update to upstream 2.1.

* Fri May 31 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-12
- Add alias org.apache.felix:felix

* Fri May 31 2013 Marek Goldmann <mgoldman@redhat.com> - 1.2.1-12
- Cleanup
- New guidelines
- felix-parent has many unnecessary Requires, RHBZ#969299

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2.1-10
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Dec 18 2012 Michal Srb <msrb@redhat.com> - 1.2.1-9
- Removed dependency on maven-site-plugin

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2.1-6
- Fix faulty compiler plugin settings setting source but not target.

* Sun Mar 13 2011 Mat Booth <fedora@matbooth.co.uk> 1.2.1-5
- Add dep on maven-plugin-jxr.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 27 2010 Mat Booth <fedora@matbooth.co.uk> - 1.2.1-3
- Add legacy depmap from maven2-common-poms for felix packages that still
  specify "felix" instead of "felix-parent"

* Tue Jul 20 2010 Hui Wang <huwang@redhat.com> - 1.2.1-2
- Update summary and description
- Add comment in mvn-jpp

* Fri Jul 16 2010 Hui Wang <huwang@redhat.com> - 1.2.1-1
- Initial version of the package

