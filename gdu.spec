Name:           gdu
Version:        5.31.0
Release:        1
Summary:        Pretty fast disk usage analyzer written in Go

License:        MIT
URL:            https://github.com/dundee/gdu

Source0:        https://github.com/dundee/gdu/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
BuildRequires:  git

Provides:       %{name} = %{version}

%description
Pretty fast disk usage analyzer written in Go.

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version}

%build
export GOINSECURE=go.opencensus.io
GO111MODULE=on CGO_ENABLED=0 go build \
-trimpath \
-buildmode=pie \
-mod=readonly \
-modcacherw \
-ldflags \
"-s -w \
-X 'github.com/dundee/gdu/v5/build.Version=v%{version}' \
-X 'github.com/dundee/gdu/v5/build.User=$(id -u -n)' \
-X 'github.com/dundee/gdu/v5/build.Time=$(LC_ALL=en_US.UTF-8 date)'" \
-o %{name} github.com/dundee/gdu/v5/cmd/gdu

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0755 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/gdu.1

%check

%post

%preun

%files
%{_bindir}/gdu
%{_mandir}/man1/gdu.1.gz

%changelog
* Thu Jun 11 2025 - Danie de Jager - 5.31.0-1
* Tue Feb 4 2025 - Danie de Jager - 5.30.1-2
- fix: set "GOINSECURE=go.opencensus.io"
* Mon Dec 30 2024 Daniel Milde - 5.30.1-1
- fix: set default colors when config file does not exist
* Mon Dec 30 2024 Daniel Milde - 5.30.0-1
- feat: show top largest files using -t or --top option in #391
- feat: introduce more style options in #396
* Mon Jun 17 2024 Daniel Milde - 5.29.0-1
- feat: support for reading gzip, bzip2 and xz files by @dundee in #363
- feat: add --show-mtime (-M) option by @dundee in #350
- feat: add option --no-unicode to disable unicode symbols by @dundee in #362
- fix: division by zero error in formatFileRow by @xroberx in #359
* Sun Apr 21 2024 Danie de Jager - 5.28.0-1
- feat: delete/empty items in background by @dundee in #336
- feat: add --show-item-count (-C) option by @ramgp in #332
- feat: add --no-delete option by @ramgp in #333
- feat: ignore item by pressing I by @dundee in #345
- feat: delete directory items in parallel by @dundee in #340
- feat: add --sequential option for sequential scanning by @dundee in #322
* Sun Feb 18 2024 Danie de Jager - 5.27.0-1
- feat: export in interactive mode by @kadogo in #298
- feat: handle vim-style navigation in confirmation by @samihda in #283
- fix: panic with Interface Conversion Nil Error by @ShivamB25 in #274
- fix: Enter key properly working when reading analysis from file by @dundee in #312
- fix: check if type matches for selected device by @dundee in #318
- ci: package gdu in docker container by @rare-magma in #313
- ci: add values for building gdu with tito by @daniejstriata in #288
- ci: change Winget Releaser job to ubuntu-latest by @sitiom in #271
* Tue Feb 13 2024 Danie de Jager - 5.26.0-1
- feat: use key-value store for analysis data in #297
- feat: use profile-guided optimization in #286
* Fri Dec 1 2023 Danie de Jager - 5.25.0-2
- Improved SPEC to build on AL2023.
* Tue Jun 6 2023 Danie de Jager - 5.25.0-1
- feat: use unicode block elements in size bar in #255
* Thu Jun 1 2023 Danie de Jager - 5.24.0-1
- feat: add ctrl+z for job control by @yurenchen000 in #250
- feat: upgrade dependencies by @dundee in #252
* Thu May 11 2023 Danie de Jager - 5.23.0-2
- Compiled with golang 1.19.9
* Tue Apr 11 2023 Danie de Jager - 5.23.0-1
- feat: added configuration option to change CWD when browsing directories by @leapfog in #230
- fix: do not show help modal when confirm modal is already opened by @dundee in #237
* Mon Feb 6 2023 Danie de Jager - 5.22.0-1
- feat: added option to follow symlinks in #206
- fix: ignore mouse events when modal is opened in #205
- Updated SPEC file used for rpm creation by @daniejstriata in #198
* Mon Jan 9 2023 Danie de Jager - 5.21.1-2
- updated SPEC file to support builds on Fedora
* Mon Jan 9 2023 Danie de Jager - 5.21.1-1
- fix: correct open command for Win
* Wed Jan 4 2023 Danie de Jager - 5.21.0-1
- feat: mark multiple items for deletion by @dundee in #193
- feat: move cursor to next row when marked by @dundee in #194
- Use GNU tar on Darwin to fix build error by @sryze in #188
* Mon Oct 24 2022 Danie de Jager - 5.20.0-1
- feat: set default sorting using config option
- feat: open file or directory in external program
- fix: check reference type
* Wed Sep 28 2022 Danie de Jager - 5.19.0-1
- feat: upgrade all dependencies
- feat: bump go version to 1.18
- feat: format negative numbers correctly
- feat: try to read config from ~/.config/gdu/gdu.yaml first
- test: export formatting
- docs: config file default locations
* Sun Sep 18 2022 Danie de Jager - 5.18.1-1
- fix: correct config file option regex
- fix: read non-default config file properly in #175
- feat: crop current item path to 70 chars in #173
- feat: show elapsed time in progress modal
- feat: configuration option for setting maximum length of the path for current item in the progress modal in #174
* Tue Sep 13 2022 Danie de Jager - 5.17.1-1
- fix: nul log file for Windows (#171)
- fix: increase the vertical size of the progress modal (#172)
- feat: added possibility to change text and background color of the selected row by @dundee in #170
* Thu Sep 8 2022 Danie de Jager - 5.16.0-1
- feat: support for reading (and writing) configuration to YAML file
- feat: initial mouse support by @dundee in #165
- add mtime for Windows by @mcoret in #157
- openbsd fixes by @dundee in #164
* Wed Aug 10 2022 Danie de Jager - 5.15.0-1
- feat: show sizes as raw numbers without prefixes by @dundee in #147
- feat: natural sorting by @dundee in #156
- fix: honor --summarize when reading analysis by @Riatre in #149
- fix: upgrade dependencies by @phanirithvij in #153
- ci: generate release tarballs with vendor directory by @CyberTailor in #148
* Mon Jul 18 2022 Danie de Jager - 5.14.0-2
* Thu May 26 2022 Danie de Jager - 5.14.0-1
- sort items by name if usage/size/count is the same (#143)
* Mon Feb 21 2022 Danie de Jager - 5.13.2
- able to go back to devices list from analyzed directory
* Thu Feb 10 2022 Danie de Jager - 5.13.1
- properly count only the first hard link size on a rescan
- do not panic if path does not start with a slash
* Sat Jan 29 2022 Danie de Jager - 5.13.0-1
- lower memory usage
- possibility to toggle between bar graph relative to the size of the directory or the biggest file
- added option --si for showing sizes with decimal SI prefixes
- fixed freeze when r key binding is being hold
* Tue Dec 14 2021 Danie de Jager - 5.12.1-1
- Bump to 5.12.1-1
- fixed listing devices on NetBSD
- escape file names (#111)
- fixed filtering
* Fri Dec 3 2021 Danie de Jager - 5.12.0-1
- Bump to 5.12.0-1
* Fri Dec 3 2021 Danie de Jager - 5.11.0-2
- Compile with go 1.17.4
* Sun Nov 28 2021 Danie de Jager - 5.11.0-1
- Bump to 5.11.0
* Tue Nov 23 2021 Danie de Jager - 5.10.1-1
- Bump to 5.10.1
* Wed Nov 10 2021 Danie de Jager - 5.10.0-1
- Bump to 5.10.01
* Mon Oct 25 2021 Danie de Jager - 5.9.0-1
- Bump to 5.9.0
* Mon Sep 27 2021 Danie de Jager - 5.8.1-2
- Remove pandoc requirement.
* Sun Sep 26 2021 Danie de Jager - 5.8.1-1
- Bump to 5.8.1
* Thu Sep 23 2021 Danie de Jager - 5.8.0-2
- Bump to 5.8.0
* Tue Sep 7 2021 Danie de Jager - 5.7.0-1
- Bump to 5.7.0
* Sat Aug 28 2021 Danie de Jager - 5.6.2-1
- Bump to 5.6.2
- Compiled with go 1.17
* Fri Aug 27 2021 Danie de Jager - 5.6.1-1
- Bump to 5.6.1
* Mon Aug 23 2021 Danie de Jager - 5.6.0-1
- Bump to 5.6.0
* Fri Aug 13 2021 Danie de Jager - 5.5.0-2
- Compiled with go 1.16.7
* Mon Aug 2 2021 Danie de Jager - 5.5.0-1
- Bump to 5.5.0
* Mon Jul 26 2021 Danie de Jager - 5.4.0-1
- Bump to 5.4.0
* Thu Jul 22 2021 Danie de Jager - 5.3.0-2
- First release
