Name:           gradle
Version:        4.3.1
Release:        10
Summary:        Build automation tool
License:        ASL 2.0
URL:            http://www.gradle.org/

BuildArch:      noarch
Source0:        http://services.gradle.org/distributions/%{name}-%{version}-src.zip
Source1:        http://services.gradle.org/versions/all#/all-released-versions.json
Source2:        gradle-font-metadata.xml
Source3:        gradle-jquery-metadata.xml
Source4:        gradle-launcher.sh
Source5:        gradle.desktop
Source6:        gradle-man.txt

Patch0001:      0001-Gradle-local-mode.patch
Patch0002:      0002-Remove-Class-Path-from-manifest.patch
Patch0003:      0003-Implement-XMvn-repository-factory-method.patch
Patch0004:      0004-Use-unversioned-dependency-JAR-names.patch
Patch0005:      0005-Port-to-Maven-3.3.9-and-Eclipse-Aether.patch
Patch0006:      0006-Disable-code-quality-checks.patch
Patch0007:      0007-Port-to-Kryo-3.0.patch
Patch0008:      0008-Port-to-Ivy-2.4.0.patch
Patch0009:      0009-Port-to-Polyglot-0.1.8.patch
Patch0010:      0010-Port-from-Simple-4-to-Jetty-9.patch
Patch0011:      0011-Disable-benchmarks.patch
Patch0012:      0012-Disable-patching-of-external-modules.patch
Patch0013:      0013-Add-missing-transitive-dependencies.patch
Patch0014:      0014-Disable-ideNative-module.patch
Patch0015:      0015-Disable-docs-build.patch
Patch0016:      0016-Port-to-guava-20.0.patch
Patch0017:      0017-Set-core-api-source-level-to-8.patch
Patch0018:      0018-Use-HTTPS-for-GoogleAPIs-repository.patch

BuildRequires:  gradle-local desktop-file-utils hostname procps-ng asciidoc xmlto
BuildRequires:  mvn(antlr:antlr) mvn(biz.aQute.bnd:bndlib)
BuildRequires:  mvn(bsh:bsh) mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(ch.qos.logback:logback-core) mvn(com.amazonaws:aws-java-sdk-core)
BuildRequires:  mvn(com.amazonaws:aws-java-sdk-kms) mvn(com.amazonaws:aws-java-sdk-s3)
BuildRequires:  mvn(com.beust:jcommander) mvn(com.esotericsoftware.kryo:kryo)
BuildRequires:  mvn(com.esotericsoftware:minlog) mvn(com.esotericsoftware:reflectasm)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.google.code.findbugs:findbugs) mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.code.gson:gson) mvn(com.google.guava:guava:20.0)
BuildRequires:  mvn(com.google.guava:guava-jdk5:20.0) mvn(com.google.http-client:google-http-client)
BuildRequires:  mvn(com.google.oauth-client:google-oauth-client)
BuildRequires:  mvn(com.googlecode.jarjar:jarjar) mvn(com.googlecode.jatl:jatl)
BuildRequires:  mvn(com.jcraft:jsch) mvn(com.puppycrawl.tools:checkstyle)
BuildRequires:  mvn(com.sun:tools) mvn(com.typesafe.zinc:zinc)
BuildRequires:  mvn(com.uwyn:jhighlight) mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-cli:commons-cli) mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-configuration:commons-configuration)
BuildRequires:  mvn(commons-io:commons-io) mvn(commons-lang:commons-lang)
BuildRequires:  mvn(dom4j:dom4j) mvn(javax.inject:javax.inject)
BuildRequires:  mvn(javax.servlet:javax.servlet-api) mvn(jaxen:jaxen)
BuildRequires:  mvn(jline:jline) mvn(joda-time:joda-time)
BuildRequires:  mvn(junit:junit) mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.jcip:jcip-annotations) mvn(net.rubygrapefruit:native-platform)
BuildRequires:  mvn(net.sourceforge.nekohtml:nekohtml) mvn(org.antlr:antlr4-runtime)
BuildRequires:  mvn(org.apache.ant:ant) mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-lang3) mvn(org.apache.geronimo.specs:geronimo-annotation_1.0_spec)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore) mvn(org.apache.ivy:ivy)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-file) mvn(org.apache.maven.wagon:wagon-http)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http-shared)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-artifact) mvn(org.apache.maven:maven-builder-support)
BuildRequires:  mvn(org.apache.maven:maven-compat) mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model) mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api) mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.maven:maven-settings) mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.apache.xbean:xbean-reflect) mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on) mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(org.codehaus.groovy.modules.http-builder:http-builder)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all) mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils) mvn(org.codenarc:CodeNarc)
BuildRequires:  mvn(org.eclipse.aether:aether-api) mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:  mvn(org.eclipse.aether:aether-impl) mvn(org.eclipse.aether:aether-spi)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-wagon)
BuildRequires:  mvn(org.eclipse.aether:aether-util) mvn(org.eclipse.jdt:core)
BuildRequires:  mvn(org.eclipse.jetty:jetty-annotations)
BuildRequires:  mvn(org.eclipse.jetty:jetty-jsp) mvn(org.eclipse.jetty:jetty-plus)
BuildRequires:  mvn(org.eclipse.jetty:jetty-security) mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet) mvn(org.eclipse.jetty:jetty-util)
BuildRequires:  mvn(org.eclipse.jetty:jetty-webapp) mvn(org.eclipse.jetty:jetty-xml)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-runtime)
BuildRequires:  mvn(org.fusesource.jansi:jansi) mvn(org.fusesource.jansi:jansi-native)
BuildRequires:  mvn(org.gmetrics:GMetrics) mvn(org.jsoup:jsoup)
BuildRequires:  mvn(org.mozilla:rhino) mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.ow2.asm:asm-all) mvn(org.parboiled:parboiled-core)
BuildRequires:  mvn(org.parboiled:parboiled-java) mvn(org.pegdown:pegdown)
BuildRequires:  mvn(org.samba.jcifs:jcifs) mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:jul-to-slf4j) mvn(org.slf4j:log4j-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api) mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.sonatype.plexus:plexus-cipher) mvn(org.sonatype.plexus:plexus-sec-dispatcher)
BuildRequires:  mvn(org.sonatype.pmaven:pmaven-common) mvn(org.sonatype.pmaven:pmaven-groovy)
BuildRequires:  mvn(org.testng:testng) mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-apis:xml-apis)
BuildRequires:  lato-fonts liberation-mono-fonts js-jquery

Requires:       javapackages-tools hicolor-icon-theme java-devel
Requires:       ant-lib apache-commons-cli apache-commons-codec apache-commons-collections
Requires:       apache-commons-compress apache-commons-io apache-commons-lang apache-commons-lang3
Requires:       apache-ivy aqute-bndlib atinject aws-sdk-java-core aws-sdk-java-kms aws-sdk-java-s3
Requires:       base64coder beust-jcommander bouncycastle bouncycastle-pg ecj glassfish-servlet-api
Requires:       google-gson google-guice groovy-lib guava20 hawtjni-runtime httpcomponents-client
Requires:       httpcomponents-core jackson-annotations jackson-core jackson-databind jansi
Requires:       jansi-native  jatl jcifs jcip-annotations jcl-over-slf4j jetty-server jetty-util
Requires:       joda-time jsch jsr-305 jul-to-slf4j junit kryo maven-lib log4j-over-slf4j
Requires:       maven-resolver-api maven-resolver-connector-basic maven-resolver-impl maven-resolver-spi
Requires:       maven-resolver-transport-wagon maven-resolver-util maven-wagon-file maven-wagon-http
Requires:       maven-wagon-http-shared maven-wagon-provider-api minlog native-platform
Requires:       nekohtml objectweb-asm objenesis plexus-cipher plexus-classworlds
Requires:       plexus-interpolation plexus-sec-dispatcher plexus-utils reflectasm rhino sisu-inject
Requires:       sisu-plexus slf4j snakeyaml tesla-polyglot-common tesla-polyglot-groovy
Requires:       testng xbean xerces-j2 xml-commons-apis

%description
Gradle is build automation evolved,which can automate the building, testing, publishing,
deployment and more of software packages.

Gradle combines the power and flexibility of Ant with the dependency management and conventions
of Maven into a more effective way to build. Powered by a Groovy DSL and packed with innovation,
Gradle provides a declarative way to describe all kinds of builds through sensible defaults.
Gradle is quickly becoming the build system of choice for many open source projects,
leading edge enterprises and legacy automation challenges.

%package help
Summary:        Help documentation of gradle package
Requires:       %{name} = %{version}-%{release}

%description help
Help documentation of gradle package.

%prep
%autosetup -n %{name}-%{version} -p1

rm -rf gradle/wrapper/subprojects/diagnostics/src/main/resources/org/gradle/api/tasks/diagnostics/htmldependencyreport/jquery.jstree.js

install -d build
cp %{SOURCE1} build/all-released-versions.json

rm -rf buildSrc/src/main/groovy/org/gradle/binarycompatibility \
buildSrc/src/main/groovy/org/gradle/build/docs/CacheableAsciidoctorTask.groovy

%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE2}
%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE3}

rm -rf buildSrc/src/test

sed -i 's/"-Werror" <<//' gradle/strictCompile.gradle

removeProject() { sed -i "/'$1'/d" settings.gradle;sed -i "s/'$1',\?//" build.gradle;}

removeProject resourcesGcs
rm -r subprojects/resources-gcs subprojects/ide-native

%build
rm gradle.properties
gradle-local --offline --no-daemon install xmvnInstall -Pgradle_installPath=$PWD/inst \
    -PfinalRelease -Dbuild.number="%{version}-%{release}"

install -d man
asciidoc -b docbook -d manpage -o man/gradle.xml %{SOURCE6}
xmlto man man/gradle.xml -o man

%install
install -d -m 755 %{buildroot}%{_javadir}/gradle/
cp subprojects/distributions/src/toplevel/NOTICE .
cp subprojects/docs/src/samples/application/src/dist/LICENSE .

rm -rf inst/bin/gradle.bat inst/media
ln -sf %{_bindir}/gradle inst/bin/gradle
find inst/lib -type f -name 'gradle*' | sed 's:.*/\(gradle-.*\)-%{version}.*:ln -sf %{_javadir}/gradle/\1.jar &:' | bash -x
ln -sf $(build-classpath ecj) inst/lib/plugins/ecj.jar
xmvn-subst -s $(find inst/lib -type f)
ln -s `find-jar commons-lang` inst/lib/
cp -a inst %{buildroot}%{_datadir}/gradle

%mvn_install
install -d -m 755 %{buildroot}%{_bindir}/
install -p -m 755 %{SOURCE4} %{buildroot}%{_bindir}/gradle

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE5}

install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

install -p -m 644 subprojects/distributions/src/toplevel/media/gradle-icon-16x16.png \
    %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/gradle.png
install -p -m 644 subprojects/distributions/src/toplevel/media/gradle-icon-24x24.png \
    %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/gradle.png
install -p -m 644 subprojects/distributions/src/toplevel/media/gradle-icon-32x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/gradle.png
install -p -m 644 subprojects/distributions/src/toplevel/media/gradle-icon-48x48.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gradle.png
install -p -m 644 subprojects/distributions/src/toplevel/media/gradle-icon-64x64.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gradle.png
install -p -m 644 subprojects/distributions/src/toplevel/media/gradle-icon-128x128.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/gradle.png
install -p -m 644 subprojects/distributions/src/toplevel/media/gradle-icon-256x256.png \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/gradle.png

install -d -m 755 %{buildroot}%{_mandir}/man1/
install -p -m 644 man/gradle.1 %{buildroot}%{_mandir}/man1/gradle.1

%files -f .mfiles
%license NOTICE LICENSE
%{_bindir}/gradle
%{_datadir}/gradle
%{_datadir}/applications/gradle.desktop
%{_datadir}/icons/hicolor/*/apps/gradle.png

%files help
%{_mandir}/man1/gradle.1*

%changelog
* Fri Dec 13 2019 daiqianwen <daiqianwen@huawei.com> - 4.3.1-10
- Package init



