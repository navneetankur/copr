Name:           dragon-drop
Version:        1.2.0
Release:        1%{?dist}
Summary:        Simple drag-and-drop source/sink for X or Wayland

License:        GPLv3
URL:            https://github.com/mwh/dragon
Source0:        https://github.com/mwh/dragon/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gtk3-devel
Requires:       gtk3

%description
dragon - simple drag-and-drop source/sink for X or Wayland

Many programs, particularly web applications, expect files to be dragged
into them now. If you don't habitually use a file manager that is a
problem. dragon is a lightweight drag-and-drop source for X where you
can run:
  dragon file.tar.gz
to get a window with just that file in it, ready to be dragged where you
need it.

%prep
%autosetup -n dragon-%version


%build
%make_build DEFINES=-g 

%install
%make_install DEFINES=-g NAME=dragon-drop PREFIX=%{_prefix}


%files
%{_bindir}/dragon-drop
%{_mandir}/man1/dragon-drop.1.gz
%license LICENCE


%changelog
* Sun May 15 2022 Navneet Aman <contact@navneetaman.com> 1.2.0-1
- initial
