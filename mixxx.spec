# The spec file contains some tips, thanks to:
# https://www.archlinux.org/packages/community/x86_64/mixxx/
# https://packages.gentoo.org/packages/media-sound/mixxx
# http://packman.links2linux.org/package/mixxx
# https://madb.mageia.org/package/show/name/mixxx
# https://mixxx.org/wiki/doku.php/compiling_on_linux

%global commit0 405b5323e8866379d033aff7f8f769d35c7e4513
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

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

%bcond_without _qt5
%bcond_without _clang

Name:           mixxx
Version:        2.1.0
Release:	2%{?gver}%{?dist}
Summary:        Everything you need to perform live DJ mixes
License:        GPLv2+
Group:          Applications/Multimedia
Url:            http://www.mixxx.org
Source0:	https://github.com/mixxxdj/mixxx/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1000:     mixxx-rpmlintrc
Patch:		multi_lib.patch

BuildRequires:  audiofile
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gperftools-devel
BuildRequires:  ladspa
BuildRequires:  lame-devel
BuildRequires:  libusb-devel
BuildRequires:  pkgconfig
BuildRequires:  portmidi-devel
BuildRequires:  scons
BuildRequires:  desktop-file-utils
BuildRequires:  util-linux
BuildRequires:  xz
BuildRequires:  chrpath
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(audiofile)
BuildRequires:  pkgconfig(flac)
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
BuildRequires:	faad2-devel
BuildRequires:	fftw-devel
BuildRequires:	coreutils
#BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(protobuf-lite)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(python-2.7)
BuildRequires:  pkgconfig(python2)
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

Requires:       qm-vamp-plugins
Recommends:     lame
Provides:       mixxx-unstable = %{version}
Obsoletes:      mixxx-unstable < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libmad-devel
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
#QT5
%if %{with _qt5}
BuildRequires:	qt5-devel
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
%setup -n %{name}-%{commit0} 

%ifarch x86_64
%patch -p1
%endif

%build

%if %{with _clang}
export CC=clang CXX=clang++
%endif

CXXFLAGS+="$RPM_OPT_FLAGS"
CFLAGS+="$RPM_OPT_FLAGS"
export SCONSFLAGS="-j $(nproc)"
export LIBDIR=%{_libdir}

scons %{?_smp_mflags} build=release optimize=portable virtualize=0 localecompare=0 qt_sqlite_plugin=1 opus=1 shoutcast=1 prefix=%{_prefix} faad=1 verbose=0 ogg=1 ipod=0 machine=%{machine} \
%if %{with _qt5}
qt5=1 \
qtdir=%{_qt5_prefix} \
%else
qtdir=%{_qt4_prefix} \
%endif

%install
%if %{with _clang}
export CC=clang CXX=clang++
%endif
scons %{?_smp_mflags} verbose=0 prefix=%{_prefix} install_root=%{buildroot}/usr \
%if %{with _qt5}
qt5=1 \
qtdir=%{_qt5_prefix} \
%endif
install


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
install -p -m 0644 res/linux/mixxx.usb.rules %{buildroot}/%{_udevrulesdir}/90-mixxx.usb.rules

# Remove rpath.
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/mixxx/plugins/vamp/libmixxxminimal.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/mixxx/plugins/soundsource/libsoundsourcem4a.so
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/mixxx

# FIX wrong-script-interpreter
sed -i 's|/usr/bin/env php|/usr/bin/php|g' %{buildroot}/%{_datadir}/mixxx/controllers/convertToXMLSchemaV1.php

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING LICENSE Mixxx-Manual.pdf README*
%{_bindir}/mixxx
%{_libdir}/mixxx/
%{_datadir}/mixxx/
%exclude %{_datadir}/mixxx/translations/
%{_datadir}/applications/mixxx.desktop
%{_datadir}/pixmaps/mixxx-icon.png
%{_datadir}/appdata/mixxx.appdata.xml
%{_udevrulesdir}/90-mixxx.usb.rules

%changelog

* Wed Oct 11 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 2.1.0-2-git405b532
- Rebuilt for soundtouch

* Mon Sep 11 2017 David Vásquez <davidva AT tutanota DOT com> - 2.1.0-1-gitd01523c
- Initial build
