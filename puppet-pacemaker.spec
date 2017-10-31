%{!?upstream_version: %global upstream_version %{commit}}
%if 0%{?dlrn}
%define upstream_name openstack-pacemaker
%else
%define upstream_name puppet-pacemaker
%endif
%global commit e0f9c4253abce26de340a8c8256c87f5c9f27e02
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-pacemaker
Version:        0.6.0
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet module for Pacemaker
License:        ASL 2.0

URL:            https://github.com/redhat-openstack/puppet-pacemaker

Source0:        https://github.com/openstack/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-firewall
Requires:       puppet >= 2.7.0

%description
Puppet module for Pacemaker

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/pacemaker/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/pacemaker/



%files
%{_datadir}/openstack-puppet/modules/pacemaker/


%changelog
* Sat Aug 26 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.6.0-1.e0f9c425git
- Pike update 0.6.0 (e0f9c4253abce26de340a8c8256c87f5c9f27e02)



