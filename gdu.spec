Name:           gdu
Version:        5.38.0
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
