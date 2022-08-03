Name:           makehuman
Version:        1.2.0.2022.08.03
Release:        1%{?dist}
Summary:        computer graphics middleware designed for the prototyping of photorealistic humanoids.

License:        AGPL
%global giturl https://github.com/makehumancommunity/makehuman
URL:            %giturl

BuildRequires:  git-lfs python3
Requires:       python3-numpy python3-qt5 python3-pyopengl

%description
MakeHuman is a computer graphics middleware designed for the prototyping of photorealistic humanoids.


%prep
git clone --depth 1 %giturl %name
%setup -DTn %name
cd makehuman
./download_assets_git.py


%install
mkdir -p %buildroot/%_datadir
mkdir -p %buildroot/%_bindir
cp -r makehuman %buildroot/%_datadir
cd %buildroot/%_bindir
ln -s ../share/%name/%{name}.py %name

%files
%_bindir/%name
%_datadir/%name
%license LICENSE.ASSETS.md LICENSE.CODE.md LICENSE.md



%changelog
* Wed Aug 03 2022 Navneet Aman <contact@navneetaman.com> - 1.2.0.2022.08.03
- init
