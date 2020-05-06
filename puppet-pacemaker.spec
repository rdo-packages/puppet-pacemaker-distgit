%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           puppet-pacemaker
Version:        0.8.0
Release:        1%{?dist}
Summary:        Puppet module for Pacemaker
License:        ASL 2.0

URL:            https://github.com/openstack/puppet-pacemaker

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-firewall
Requires:       puppet >= 2.7.0

%description
Puppet module for Pacemaker

%prep
%setup -q -n openstack-pacemaker-%{upstream_version}

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
* Wed May 06 2020 RDO <dev@lists.rdoproject.org> 0.8.0-1
- Update to 0.8.0



