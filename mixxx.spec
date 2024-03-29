# The spec file contains some tips, thanks to:
# https://www.archlinux.org/packages/community/x86_64/mixxx/
# https://packages.gentoo.org/packages/media-sound/mixxx
# http://packman.links2linux.org/package/mixxx
# https://madb.mageia.org/package/show/name/mixxx
# https://mixxx.org/wiki/doku.php/compiling_on_linux

%global commit0 96fc5dd217a81d0e2327a52f564f7aea7d5c2c43
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

%global  _hardened_build     1
#global _disable_ld_no_undefined %nil
%undefine __cmake_in_source_build

%ifarch i686
%global machine i686
%endif
%ifarch x86_64
%global machine amd64
%endif
%ifarch armv5tl
%global machine armel
%endif
%ifarch armv7hl
%global machine armhf
%endif


# Conditional Clang
%bcond_with _clang

# Python3 migration coming soon
%bcond_with _py2

# Conditional qt5 
%bcond_without _qt5


Name:           mixxx
Version:        2.3.2
Release:	7%{?gver}%{?dist}
Summary:        Everything you need to perform live DJ mixes
License:        GPLv2+
Group:          Applications/Multimedia
Url:            http://www.mixxx.org
Source0:	https://github.com/mixxxdj/mixxx/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch:		benchmark_compile_fix.patch

BuildRequires:  audiofile
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gperftools-devel
BuildRequires:  ladspa
BuildRequires:  lame-devel
BuildRequires:  libusb-devel
BuildRequires:  pkgconfig
BuildRequires:  portmidi-devel
BuildRequires:  ffmpeg-devel >= 5.0
BuildRequires:  desktop-file-utils
BuildRequires:  util-linux
BuildRequires:  xz
BuildRequires:  git
BuildRequires:  chrpath
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(audiofile)
BuildRequires:  pkgconfig(flac)
BuildRequires:	hidapi-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel 
BuildRequires:  protobuf-compiler
BuildRequires:  libebur128-devel
BuildRequires:  libkeyfinder-devel
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(jack) >= 0.109
BuildRequires:  pkgconfig(libchromaprint)
#BuildRequires:  pkgconfig(libmusicbrainz)
%if %{with _clang}
BuildRequires:  clang
%endif
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:	sqlite-devel
BuildRequires:	libmp4v2-devel
BuildRequires:	faad2-devel >= 2.9.1
BuildRequires:	fftw-devel
BuildRequires:	coreutils
#BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(protobuf-lite)
%if %{with _py2}
BuildRequires:	python2-devel
%else
BuildRequires:	python3-devel
%endif
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(shout)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soundtouch) >= 1.3
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(taglib_c)
BuildRequires:  pkgconfig(vamp)
BuildRequires:  pkgconfig(vamp-hostsdk)
BuildRequires:  pkgconfig(vamp-sdk)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(zlib)
%if 0%{?fedora} >= 36
BuildRequires:	annobin-plugin-gcc
%endif

Requires:       qm-vamp-plugins
Recommends:     lame
Provides:       mixxx-unstable = %{version}
Obsoletes:      mixxx-unstable < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:	gcc-c++
BuildRequires:  libmad-devel
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:	lilv-devel
#QT5
%if %{with _qt5}
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-qtbase
BuildRequires:	qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5ScriptTools)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  cmake(Qt5Keychain)
#QT4
%else
BuildRequires:  pkgconfig(Qt3Support) >= 4.8
BuildRequires:  pkgconfig(QtCLucene) >= 4.8
BuildRequires:  pkgconfig(QtCore) >= 4.8
BuildRequires:  pkgconfig(QtDBus) >= 4.8
BuildRequires:  pkgconfig(QtDeclarative) >= 4.8
BuildRequires:  pkgconfig(QtDesigner) >= 4.8
BuildRequires:  pkgconfig(QtDesignerComponents) >= 4.8
BuildRequires:  pkgconfig(QtGui) >= 4.8
BuildRequires:  pkgconfig(QtHelp) >= 4.8
BuildRequires:  pkgconfig(QtMultimedia) >= 4.8
BuildRequires:  pkgconfig(QtNetwork) >= 4.8
BuildRequires:  pkgconfig(QtOpenGL) >= 4.8
BuildRequires:  pkgconfig(QtScript) >= 4.8
BuildRequires:  pkgconfig(QtScriptTools) >= 4.8
BuildRequires:  pkgconfig(QtSql) >= 4.8
BuildRequires:  pkgconfig(QtSvg) >= 4.8
BuildRequires:  pkgconfig(QtTest) >= 4.8
BuildRequires:  pkgconfig(QtUiTools) >= 4.8
BuildRequires:  pkgconfig(QtWebKit)
BuildRequires:  pkgconfig(QtXml) >= 4.8
BuildRequires:  pkgconfig(QtXmlPatterns) >= 4.8
%endif

%description
Mixxx is free DJ software that gives you everything you need to perform 
live DJ mixes. Blend songs together with automatic BPM matching and remix 
on-the-fly with looping and hot cues. Whether you're a pro DJ or just getting
started, Mixxx has you covered.

Mixxx works with ALSA, JACK, OSS and supports many popular DJ controllers.

%prep
%autosetup -n %{name}-%{commit0} -p1


%build

%if %{with _py2}
find ./ -type f -name \*.py -exec sed -i 's|/usr/bin/env python|/usr/bin/python2|g' {} \;
%else
find ./ -type f -name \*.py -exec sed -i 's|/usr/bin/env python|/usr/bin/python3|g' {} \;
%endif

%if %{with _clang}
export CC=clang CXX=clang++
%endif

mkdir -p build
%cmake -B build \
        -DQTKEYCHAIN=ON \
        -DOPTIMIZE=OFF \
        -DOPTIMIZE=portable 

%install

%if %{with _clang}
export CC=clang CXX=clang++
%endif

%make_install -C build 

rm -rf "%{buildroot}%{_datadir}/doc/mixxx"

# remove .orig files, not permitted
find "%{buildroot}%{_datadir}/mixxx/skins/" -type f -name '*.orig' -delete

# fix perms
find "%{buildroot}%{_datadir}/mixxx/" -type f -executable \( -name '*.xml' -o -name '*.js' -o -name '*.txt' \) \
-exec chmod 0644 {} \;

%find_lang %{name} --with-qt

# hardlinks are required to speedup build
%fdupes "%{buildroot}%{_datadir}/mixxx/skins"

# udev rules
install -d %{buildroot}/%{_udevrulesdir}
install -p -m 0644 res/linux/mixxx-usb-uaccess.rules %{buildroot}/%{_udevrulesdir}/90-mixxx.usb.rules

# Remove rpath.
#chrpath --delete $RPM_BUILD_ROOT%{_libdir}/mixxx/plugins/vamp/libmixxxminimal.so
#chrpath --delete $RPM_BUILD_ROOT%{_bindir}/mixxx

# FIX wrong-script-interpreter
#sed -i 's|/usr/bin/env php|/usr/bin/php|g' %{buildroot}/%{_datadir}/mixxx/controllers/convertToXMLSchemaV1.php

# Delete version-control-internal-file
rm -f %{buildroot}/%{_datadir}/mixxx/controllers/novation-launchpad/.gitignore

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING LICENSE README*
%{_bindir}/mixxx
%{_datadir}/mixxx/
%exclude %{_datadir}/mixxx/translations/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/mixxx.png
%{_datadir}/icons/hicolor/*/apps/mixxx.svg
%{_datadir}/metainfo/*.metainfo.xml
/usr/lib/udev/rules.d/*.rules


%changelog

* Tue Feb 08 2022 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.3.2-7-git96fc5dd
- Updated to 2.3.2

* Mon Oct 04 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.3.1-7-git8acb633
- Updated to 2.3.1

* Mon Jul 05 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.3.0-7-gitd1dca47
- Updated to 2.3.0

* Mon Oct 05 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.2.4-8-git5968348
- Rebuilt

* Sun May 17 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.2.4-7-git5968348
- Updated to 2.2.4

* Tue Dec 10 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.2.3-7-git4d3d17d
- Updated to 2.2.3

* Fri Nov 08 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.2.2-8-git8a94cf5
- Rebuilt for faad2

* Wed Aug 14 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.2.2-7-git8a94cf5
- Updated to 2.2.2

* Tue Apr 23 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.2.1-7-git286a52a
- Updated to 2.2.1

* Mon Oct 29 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.2.0-2-git1b5b522
- Updated to 2.2.0

* Fri Aug 24 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.1.70-3-git2689787
- Update to current commit

* Thu May 24 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.1.70-2-git0984215
- Updated to current commit
- Preparing the migration to tq5

* Sun Feb 04 2018 David Vásquez <davidva AT tutanota DOT com> - 2.1.70-1-git5667a0d
- Updated to 2.1.70-1-git5667a0d

* Thu Nov 23 2017 David Vásquez <davidva AT tutanota DOT com> - 2.1.0-3-gita959f40
- Updated to 2.1.0-3-gita959f40

* Thu Oct 12 2017 David Vásquez <davidva AT tutanota DOT com> - 2.1.0-2-git405b532
- Updated to current commit
- Scons local conditional

* Mon Sep 11 2017 David Vásquez <davidva AT tutanota DOT com> - 2.1.0-1-gitd01523c
- Initial build
