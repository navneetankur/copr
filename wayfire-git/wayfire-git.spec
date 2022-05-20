Name:           wayfire-git
Version:        0.7.3.2022.05.20
Release:        2%{?dist}
Summary:        3D wayland compositor
License:        MIT
URL:            https://github.com/WayfireWM/wayfire

%global src0    wayfire
Source0:        %src0.tar.gz

BuildRequires:  git-core
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  inotify-tools-devel
BuildRequires:  libevdev-devel
BuildRequires:  meson >= 0.53.0

BuildRequires:  cmake(doctest)
BuildRequires:  cmake(glm)

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput) >= 1.7.0
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots) >= 0.15.0, pkgconfig(wlroots) < 0.16.0
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(nlohmann_json)

Recommends:     wayfire-config-manager
Recommends:     wf-shell

Provides:       bundled(wf-touch) = %version
Provides:       bundled(wf-utils) = %version
Provides:       bundled(wf-config) = %version
Conflicts:      wayfire
Provides:       wayfire = %version

%description
Wayfire is a wayland compositor based on wlroots. It aims to create a
customizable, extendable and lightweight environment without sacrificing its
appearance.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%prep
%setup -n %src0

%build
%meson                            \
    -Duse_system_wfconfig=disabled \
    -Duse_system_wlroots=enabled  \
    %{nil}
%meson_build


%install
%meson_install
rm -f %{buildroot}%{_libdir}/libwftouch.a
rm -f %{buildroot}/%{_prefix}/lib/debug/usr/lib64/libwf-config.so.0.8.0-0.7.3-1.fc36.x86_64.debug


%files
%license LICENSE
%doc README.md %{src0}.ini
%{_bindir}/%{src0}
%{_datadir}/%{src0}/
%{_datadir}/wayland-sessions/*.desktop
%{_libdir}/%{src0}/
%{_libdir}/libwf-utils.so.0*
%{_libdir}/libwf-config.so
%{_libdir}/libwf-config.so.0.8.0
%{_libdir}/libwf-config.so.1

%files devel
%{_libdir}/libwf-utils.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{src0}/


%changelog
* Fri May 20 2022 Navneet Aman <contact@navneetaman.com> - 0.7.3.2022.05.20-2
- Use git submodules for wf-utils,wf-touch and wf-config
* Fri May 20 2022 Navneet Aman <contact@navneetaman.com> - 0.7.3.2022.05.20-1
- Git package
