Name:           wayfire-git
Version:        0.7.3.2022.05.20
Release:        1%{?dist}
Summary:        3D wayland compositor
License:        MIT
URL:            https://github.com/WayfireWM/wayfire

%global src0    wayfire
%global src1    wf-utils
%global src2    wf-config
%global src3    wf-touch
%global branch  master

%global dl0     https://github.com/WayfireWM/%{src0}/archive/refs/heads/%branch.zip
%global dl1     https://github.com/WayfireWM/%{src1}/archive/refs/heads/%branch.zip
%global dl2     https://github.com/WayfireWM/%{src2}/archive/refs/heads/%branch.zip
%global dl3     https://github.com/WayfireWM/%{src3}/archive/refs/heads/%branch.zip

Source0:        empty

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
curl -Lo %src0-%branch.zip %dl0
curl -Lo %src1-%branch.zip %dl1
curl -Lo %src2-%branch.zip %dl2
curl -Lo %src3-%branch.zip %dl3
unzip -qqo %src0-%branch.zip
%setup -DTn %src0-%branch
unzip -qqo ../%src1-%branch.zip
mv %src1-%branch/* subprojects/%src1/
unzip -qqo ../%src2-%branch.zip
mv %src2-%branch/* subprojects/%src2/
unzip -qqo ../%src3-%branch.zip
mv %src3-%branch/* subprojects/%src3/

%build
%meson                            \
    -Duse_system_wfconfig=disabled \
    -Duse_system_wlroots=enabled  \
    %{nil}
%meson_build


%install
%meson_install
install -Dpm0644 %{src0}.desktop %{buildroot}%{_datadir}/wayland-sessions/%{name}.desktop
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
* Fri May 20 2022 Navneet Aman <contact@navneetaman.com> - 0.7.3.2022.05.20-1
- Git package
