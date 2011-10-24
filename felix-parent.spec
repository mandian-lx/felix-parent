Name:           felix-parent
Version:        1.2.1
Release:        5
Summary:        Parent POM file for Apache Felix Specs

Group:          Development/Java
License:        ASL 2.0
URL:            http://felix.apache.org/
#svn export http://svn.apache.org/repos/asf/felix/releases/felix-parent-1.2.1/
#tar -jcf felix-parent-1.2.1.tar.bz2 felix-parent-1.2.1/
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-depmap.xml
#Remove mockito-all dependency which is not in koji
Patch0:        %{name}-%{version}-pom.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: junit
BuildRequires: easymock2
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-deploy-plugin
BuildRequires: maven-gpg-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-project-info-reports-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-report-maven-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-jxr

Requires: junit
Requires: easymock2
Requires: maven-plugin-plugin
Requires: maven-compiler-plugin
Requires: maven-install-plugin
Requires: maven-jar-plugin
Requires: maven-javadoc-plugin
Requires: maven-resources-plugin
Requires: maven-assembly-plugin
Requires: maven-source-plugin
Requires: maven-deploy-plugin
Requires: maven-gpg-plugin
Requires: maven-site-plugin
Requires: maven-project-info-reports-plugin
Requires: maven-release-plugin
Requires: maven-surefire-maven-plugin
Requires: maven-surefire-report-maven-plugin
Requires: maven-plugin-build-helper
Requires: maven-plugin-jxr

Requires:       jpackage-utils
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils


%description
Parent POM file for Apache Felix Specs.

%prep
%setup -q #You may need to update this according to your Source0
%patch0 -p0

%build
#mvn-jpp call is not really needed for the pom file. 
#But it's good to have it there to see changes in dependencies when new version is released
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp \
        -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install
rm -rf %{buildroot}

# depmap
%add_to_maven_depmap org.apache.felix %{name} %{version} JPP/felix %{name}

# legacy depmap
# (some upstream packages haven't caught up with the "felix" -> "felix-parent" rename yet)
%add_to_maven_depmap org.apache.felix felix %{version} JPP/felix %{name}

# poms
install -pD -T -m 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.felix-%{name}.pom

%post
%update_maven_depmap

%postun
%update_maven_depmap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE NOTICE
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*


