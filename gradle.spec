%bcond_with bootstrap
Name:                gradle
Version:             4.4.1
Release:             1
Summary:             Build automation tool
License:             ASL 2.0
URL:                 http://www.gradle.org/
BuildArch:           noarch
Source0:             http://services.gradle.org/distributions/gradle-%{version}-src.zip
Source1:             http://services.gradle.org/versions/all#/all-released-versions.json
Source2:             gradle-font-metadata.xml
Source3:             gradle-jquery-metadata.xml
Source4:             gradle-launcher.sh
Source5:             gradle.desktop
Source6:             gradle-man.txt
Source7:             gradle-bootstrap.sh
Source8:             gradle-bootstrap-module-list
Source9:             gradle-bootstrap-module-dependencies
Source10:            gradle-bootstrap-api-mapping.txt
Source11:            gradle-bootstrap-default-imports.txt
Source12:            gradle-bootstrap-plugin.properties
Source13:            gradle-bootstrap-implementation-plugin.properties
Source14:            gradle-bootstrap-api-relocated.txt
Source15:            gradle-bootstrap-test-kit-relocated.txt
Patch0001:           0001-Gradle-local-mode.patch
Patch0002:           0002-Remove-Class-Path-from-manifest.patch
Patch0003:           0003-Implement-XMvn-repository-factory-method.patch
Patch0004:           0004-Use-unversioned-dependency-JAR-names.patch
Patch0005:           0005-Port-to-Maven-3.3.9-and-Eclipse-Aether.patch
Patch0006:           0006-Disable-code-quality-checks.patch
Patch0007:           0007-Port-to-Kryo-3.0.patch
Patch0008:           0008-Port-to-Ivy-2.4.0.patch
Patch0009:           0009-Port-to-Polyglot-0.1.8.patch
Patch0010:           0010-Port-from-Simple-4-to-Jetty-9.patch
Patch0011:           0011-Disable-benchmarks.patch
Patch0012:           0012-Disable-patching-of-external-modules.patch
Patch0013:           0013-Add-missing-transitive-dependencies.patch
Patch0014:           0014-Disable-ideNative-module.patch
Patch0015:           0015-Disable-docs-build.patch
Patch0016:           0016-Port-to-guava-20.0.patch
Patch0017:           0017-Set-core-api-source-level-to-8.patch
Patch0018:           0018-Use-HTTPS-for-GoogleAPIs-repository.patch
BuildRequires:       git
%if %{with bootstrap}
BuildRequires:       groovy >= 2.3 javapackages-local
%else
BuildRequires:       gradle-local
%endif
BuildRequires:       desktop-file-utils glibc-langpack-en hostname procps-ng
BuildRequires:       asciidoc xmlto
BuildRequires:       mvn(antlr:antlr) mvn(biz.aQute.bnd:bndlib) mvn(bsh:bsh)
BuildRequires:       mvn(ch.qos.logback:logback-classic) mvn(ch.qos.logback:logback-core)
BuildRequires:       mvn(com.amazonaws:aws-java-sdk-core) mvn(com.amazonaws:aws-java-sdk-kms)
BuildRequires:       mvn(com.amazonaws:aws-java-sdk-s3) mvn(com.beust:jcommander)
BuildRequires:       mvn(com.esotericsoftware.kryo:kryo) mvn(com.esotericsoftware:minlog)
BuildRequires:       mvn(com.esotericsoftware:reflectasm)
BuildRequires:       mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:       mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:       mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:       mvn(com.google.code.findbugs:findbugs) mvn(com.google.code.findbugs:jsr305)
BuildRequires:       mvn(com.google.code.gson:gson) mvn(com.google.guava:guava:20.0)
BuildRequires:       mvn(com.google.guava:guava-jdk5:20.0)
BuildRequires:       mvn(com.google.http-client:google-http-client)
BuildRequires:       mvn(com.google.oauth-client:google-oauth-client)
BuildRequires:       mvn(com.googlecode.jarjar:jarjar) mvn(com.googlecode.jatl:jatl)
BuildRequires:       mvn(com.jcraft:jsch) mvn(com.sun:tools) mvn(com.typesafe.zinc:zinc)
BuildRequires:       mvn(com.uwyn:jhighlight) mvn(commons-beanutils:commons-beanutils)
BuildRequires:       mvn(commons-cli:commons-cli) mvn(commons-codec:commons-codec)
BuildRequires:       mvn(commons-collections:commons-collections)
BuildRequires:       mvn(commons-configuration:commons-configuration) mvn(commons-io:commons-io)
BuildRequires:       mvn(commons-lang:commons-lang) mvn(dom4j:dom4j) mvn(javax.inject:javax.inject)
BuildRequires:       mvn(javax.servlet:javax.servlet-api) mvn(jaxen:jaxen) mvn(jline:jline)
BuildRequires:       mvn(joda-time:joda-time) mvn(junit:junit) mvn(net.java.dev.jna:jna)
BuildRequires:       mvn(net.jcip:jcip-annotations) mvn(net.rubygrapefruit:native-platform)
BuildRequires:       mvn(net.sourceforge.nekohtml:nekohtml) mvn(org.antlr:antlr4-runtime)
BuildRequires:       mvn(org.apache.ant:ant) mvn(org.apache.ant:ant-launcher)
BuildRequires:       mvn(org.apache.commons:commons-compress) mvn(org.apache.commons:commons-lang3)
BuildRequires:       mvn(org.apache.geronimo.specs:geronimo-annotation_1.0_spec)
BuildRequires:       mvn(org.apache.httpcomponents:httpclient)
BuildRequires:       mvn(org.apache.httpcomponents:httpcore) mvn(org.apache.ivy:ivy)
BuildRequires:       mvn(org.apache.maven.wagon:wagon-file) mvn(org.apache.maven.wagon:wagon-http)
BuildRequires:       mvn(org.apache.maven.wagon:wagon-http-shared)
BuildRequires:       mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:       mvn(org.apache.maven:maven-aether-provider)
BuildRequires:       mvn(org.apache.maven:maven-artifact)
BuildRequires:       mvn(org.apache.maven:maven-builder-support) mvn(org.apache.maven:maven-compat)
BuildRequires:       mvn(org.apache.maven:maven-core) mvn(org.apache.maven:maven-model)
BuildRequires:       mvn(org.apache.maven:maven-model-builder)
BuildRequires:       mvn(org.apache.maven:maven-plugin-api)
BuildRequires:       mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:       mvn(org.apache.maven:maven-settings)
BuildRequires:       mvn(org.apache.maven:maven-settings-builder)
BuildRequires:       mvn(org.apache.xbean:xbean-reflect) mvn(org.apache:apache:pom:)
BuildRequires:       mvn(org.bouncycastle:bcpg-jdk15on) mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:       mvn(org.codehaus.groovy.modules.http-builder:http-builder)
BuildRequires:       mvn(org.codehaus.groovy:groovy-all) mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:       mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:       mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:       mvn(org.codehaus.plexus:plexus-utils) mvn(org.codenarc:CodeNarc)
BuildRequires:       mvn(org.eclipse.aether:aether-api)
BuildRequires:       mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:       mvn(org.eclipse.aether:aether-impl) mvn(org.eclipse.aether:aether-spi)
BuildRequires:       mvn(org.eclipse.aether:aether-transport-wagon)
BuildRequires:       mvn(org.eclipse.aether:aether-util) mvn(org.eclipse.jdt:core)
BuildRequires:       mvn(org.eclipse.jetty:jetty-annotations) mvn(org.eclipse.jetty:jetty-jsp)
BuildRequires:       mvn(org.eclipse.jetty:jetty-plus) mvn(org.eclipse.jetty:jetty-security)
BuildRequires:       mvn(org.eclipse.jetty:jetty-server) mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:       mvn(org.eclipse.jetty:jetty-util) mvn(org.eclipse.jetty:jetty-webapp)
BuildRequires:       mvn(org.eclipse.jetty:jetty-xml) mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires:       mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:       mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:       mvn(org.fusesource.hawtjni:hawtjni-runtime) mvn(org.fusesource.jansi:jansi)
BuildRequires:       mvn(org.fusesource.jansi:jansi-native) mvn(org.gmetrics:GMetrics)
BuildRequires:       mvn(org.jsoup:jsoup) mvn(org.mozilla:rhino) mvn(org.objenesis:objenesis)
BuildRequires:       mvn(org.ow2.asm:asm-all) mvn(org.parboiled:parboiled-core)
BuildRequires:       mvn(org.parboiled:parboiled-java) mvn(org.pegdown:pegdown)
BuildRequires:       mvn(org.samba.jcifs:jcifs) mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:       mvn(org.slf4j:jul-to-slf4j) mvn(org.slf4j:log4j-over-slf4j)
BuildRequires:       mvn(org.slf4j:slf4j-api) mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:       mvn(org.sonatype.plexus:plexus-cipher)
BuildRequires:       mvn(org.sonatype.plexus:plexus-sec-dispatcher)
BuildRequires:       mvn(org.sonatype.pmaven:pmaven-common) mvn(org.sonatype.pmaven:pmaven-groovy)
BuildRequires:       mvn(org.testng:testng) mvn(xerces:xercesImpl) mvn(xml-apis:xml-apis)
BuildRequires:       lato-fonts liberation-mono-fonts js-jquery
Requires:            javapackages-tools bash hicolor-icon-theme
Recommends:          java-devel
Requires:            ant-lib apache-commons-cli apache-commons-codec apache-commons-collections
Requires:            apache-commons-compress apache-commons-io apache-commons-lang
Requires:            apache-commons-lang3 apache-ivy aqute-bndlib atinject aws-sdk-java-core
Requires:            aws-sdk-java-kms aws-sdk-java-s3 base64coder beust-jcommander bouncycastle
Requires:            bouncycastle-pg bsh ecj glassfish-servlet-api google-gson google-guice
Requires:            groovy-lib guava20 hawtjni-runtime httpcomponents-client httpcomponents-core
Requires:            jackson-annotations jackson-core jackson-databind jansi jansi-native jatl jcifs
Requires:            jcip-annotations jcl-over-slf4j jetty-server jetty-util jgit joda-time jsch
Requires:            jsr-305 jul-to-slf4j junit kryo log4j-over-slf4j maven-lib maven-resolver-api
Requires:            maven-resolver-connector-basic maven-resolver-impl maven-resolver-spi
Requires:            maven-resolver-transport-wagon maven-resolver-util maven-wagon-file
Requires:            maven-wagon-http maven-wagon-http-shared maven-wagon-provider-api minlog
Requires:            native-platform nekohtml objectweb-asm objenesis plexus-cipher
Requires:            plexus-classworlds plexus-containers-component-annotations plexus-interpolation
Requires:            plexus-sec-dispatcher plexus-utils reflectasm rhino sisu-inject sisu-plexus
Requires:            slf4j snakeyaml tesla-polyglot-common tesla-polyglot-groovy testng xbean
Requires:            xerces-j2 xml-commons-apis
%description
Gradle is build automation evolved. Gradle can automate the building,
testing, publishing, deployment and more of software packages or other
types of projects such as generated static websites, generated
documentation or indeed anything else.
Gradle combines the power and flexibility of Ant with the dependency
management and conventions of Maven into a more effective way to
build. Powered by a Groovy DSL and packed with innovation, Gradle
provides a declarative way to describe all kinds of builds through
sensible defaults. Gradle is quickly becoming the build system of
choice for many open source projects, leading edge enterprises and
legacy automation challenges.

%prep
%autosetup -S git
rm -rf gradle/wrapper/
>subprojects/diagnostics/src/main/resources/org/gradle/api/tasks/diagnostics/htmldependencyreport/jquery.jstree.js
mkdir -p build
cp %{SOURCE1} build/all-released-versions.json
rm -r buildSrc/src/main/groovy/org/gradle/binarycompatibility
rm buildSrc/src/main/groovy/org/gradle/build/docs/CacheableAsciidoctorTask.groovy
%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE2}
%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE3}
rm -rf buildSrc/src/test
sed -i 's/"-Werror" <<//' gradle/strictCompile.gradle
removeProject() {
sed -i "/'$1'/d" settings.gradle
sed -i "s/'$1',\?//" build.gradle
}
removeProject resourcesGcs
rm -r subprojects/resources-gcs
rm -r subprojects/ide-native

%build
export LANG=en_US.UTF8
%if %{with bootstrap}
mkdir -p subprojects/docs/src/main/resources
mkdir -p subprojects/core/src/main/resources/org/gradle/api/internal/runtimeshaded
cp %{SOURCE10} subprojects/docs/src/main/resources/api-mapping.txt
cp %{SOURCE11} subprojects/docs/src/main/resources/default-imports.txt
cp %{SOURCE12} subprojects/core/src/main/resources/gradle-plugins.properties
cp %{SOURCE13} subprojects/core/src/main/resources/gradle-implementation-plugins.properties
cp %{SOURCE14} subprojects/core/src/main/resources/org/gradle/api/internal/runtimeshaded/api-relocated.txt
cp %{SOURCE15} subprojects/core/src/main/resources/org/gradle/api/internal/runtimeshaded/test-kit-relocated.txt
%{SOURCE7} %{SOURCE8} %{SOURCE9}
%else
rm gradle.properties
gradle-local --offline --no-daemon install xmvnInstall \
    -Pgradle_installPath=$PWD/inst \
    -PfinalRelease -Dbuild.number="%{version}-%{release}"
%endif
mkdir man
asciidoc -b docbook -d manpage -o man/gradle.xml %{SOURCE6}
xmlto man man/gradle.xml -o man

%install
cp subprojects/distributions/src/toplevel/NOTICE .
cp subprojects/docs/src/samples/application/src/dist/LICENSE .
install -d -m 755 %{buildroot}%{_javadir}/%{name}/
%if %{with bootstrap}
cp -r bootstrap-home %{buildroot}%{_datadir}/%{name}
for mod in launcher base-services core core-api dependency-management resources \
        logging base-services-groovy model-core; do
    %mvn_file ":{gradle-$mod}" %{name}/@1 %{_datadir}/lib/@1
    %mvn_artifact org.gradle:gradle-$mod:%{version} bootstrap-home/lib/gradle-$mod.jar
done
%else # non-bootstrap
rm -rf inst/bin/gradle.bat inst/media
ln -sf %{_bindir}/%{name} inst/bin/gradle
find inst/lib -type f -name 'gradle*' | sed 's:.*/\(gradle-.*\)-%{version}.*:ln -sf %{_javadir}/%{name}/\1.jar &:' | bash -x
ln -sf $(build-classpath ecj) inst/lib/plugins/ecj.jar
xmvn-subst -s $(find inst/lib -type f)
ln -s `find-jar commons-lang` inst/lib/
cp -a inst %{buildroot}%{_datadir}/%{name}
%endif
%mvn_install
install -d -m 755 %{buildroot}%{_bindir}/
install -p -m 755 %{SOURCE4} %{buildroot}%{_bindir}/%{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE5}
for r in 16 24 32 48 64 128 256; do
    install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/
    install -p -m 644 subprojects/distributions/src/toplevel/media/gradle-icon-${r}x${r}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/%{name}.png
done
install -d -m 755 %{buildroot}%{_mandir}/man1/
install -p -m 644 man/gradle.1 %{buildroot}%{_mandir}/man1/gradle.1

%files -f .mfiles
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/gradle.1*
%license LICENSE NOTICE

%changelog
* Fri Sep 4 2020 chengzihan <chengzihan2@huawei.com> - 4.4.1-1
- upgrade to 4.4.1-1

* Fri Dec 13 2019 daiqianwen <daiqianwen@huawei.com> - 4.3.1-10
- Package init
