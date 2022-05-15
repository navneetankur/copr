Name:           advcpmv
Version:        0.9
%global CORE_UTILS_VERSION 9.0
Release:        1%{?dist}
Summary:        Advanced Copy is a mod for the GNU cp and GNU mv tools which adds a progress bar
License:        GPLv3+
URL:            https://github.com/jarun/advcpmv
Patch0:         https://raw.githubusercontent.com/jarun/advcpmv/master/%{name}-%{version}-%{CORE_UTILS_VERSION}.patch
Source0:        https://ftp.gnu.org/gnu/coreutils/coreutils-%{CORE_UTILS_VERSION}.tar.xz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gzip
BuildRequires:  perl-interpreter
# Requires:       

%description
Advanced Copy is a mod for the GNU cp and GNU mv tools which adds a progress bar
and provides some info on what's going on. It was written by Florian Zwicke and
released under the GPL.

%prep
%setup -qn coreutils-%CORE_UTILS_VERSION
%patch0 -p1


%build
%configure
%make_build


%install
gzip -k man/cp.1 man/mv.1
install -Dm 644 man/cp.1.gz %{buildroot}/%{_mandir}/man1/cpg.1.gz
install -Dm 644 man/mv.1.gz %{buildroot}/%{_mandir}/man1/mvg.1.gz
install -Dm 755 src/cp %{buildroot}/%{_bindir}/cpg
install -Dm 755 src/mv %{buildroot}/%{_bindir}/mvg

%files
%{_bindir}/cpg
%{_bindir}/mvg
%{_mandir}/man1/cpg.1.gz
%{_mandir}/man1/mvg.1.gz
%license COPYING



%changelog
* Sun May 15 2022 Navneet Aman <contact@navneetaman.com> - 0.9-1
- Initial
