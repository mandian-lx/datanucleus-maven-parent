%{?_javapackages_macros:%_javapackages_macros}
%global commit 8e55762cef51784b0308ed4cdcfeceaadb03e1d6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           datanucleus-maven-parent
Version:        3.3
Release:        5
Summary:        DataNucleus Maven parent project 

License:        ASL 2.0
URL:            https://github.com/datanucleus/datanucleus-maven-parent
Source:         https://github.com/datanucleus/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

# jira opened for missing ASL file
# http://www.datanucleus.org/servlet/jira/browse/NUCACCESS-130
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt 

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  maven-clean-plugin
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%description
Datanucleus Maven parent pom used by other datanucleus packages.

%prep
%setup -q -n %{name}-%{commit}
cp -p %{SOURCE1} LICENSE
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin

%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-ssh-external']]"

%pom_remove_parent

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Feb 13 2017 Pete MacKinnon <pmackinn@redhat.com> - 3.3-5
- Remove oss-parent
- Add maven-plugin-bundle dep

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 12 2014 Pete MacKinnon <pmackinn@redhat.com> - 3.3-1
- Initial version
- remove wagon-ssh-external
- git commit for src
