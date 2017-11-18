%global dont_strip 1
%global __debug_install_post %{nil}
%global debug_package %{nil}

Name:           pwn-school
Version:        1.0.0
Release:        %mkrel 1
Summary:        Learning tool how to pwn badly written programs

License:        GPLv3
URL:            https://github.com/Arusekk/pwn-school
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  pythonegg(2)(python)
Requires:       pythonegg(2)(pip)
# pythonegg(2)(peda) pythonegg(2)(pwntools)
Requires:       gdb
Requires:       /bin/bash

%description
Pwn School teaches how to pwn applications with errors such as off-by-one,
helps to understand stack- and heap-overflows.

%prep
%setup

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%pre
mkdir -p /var/pwn-school
for i in `seq 1 15`; do
  %_pre_useradd pwn$i /var/pwn-school/pwn$i /bin/bash
done

%post
for i in `seq 1 15`; do
  sh /var/pwn-school/fixperm.sh /var/pwn-school/pwn$i $i
done
pip2 install peda pwntools ropper

%preun
rm /var/pwn-school/pwn?/password
rm /var/pwn-school/pwn??/password

%postun
for i in `seq 1 15`; do
  %_postun_userdel pwn$i
done

%files
%defattr(-,root,root)
%doc README.md
%config %{_sysconfdir}/gdbinit.d/020.peda.gdb
/var/pwn-school
%{_libdir}/libpwn-school.so

%changelog
* Sat Oct 21 2017 Arek <rpm@glus> - 1.0.0-1.mga5
- Initial RPM release
