%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-pacemaker
%global commit a09f5dd75bb0ee0605b013b2c604dd64e259e948
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%{?dlrn: %global tarsources openstack-pacemaker}
%{!?dlrn: %global tarsources %{name}}

Name:           puppet-pacemaker
Version:        0.8.0
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet module for Pacemaker
License:        ASL 2.0

URL:            https://github.com/openstack/puppet-pacemaker

Source0:        https://github.com/openstack/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-firewall
Requires:       puppet >= 2.7.0

%description
Puppet module for Pacemaker

%prep
%setup -q -n %{tarsources}-%{upstream_version}

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
* Wed Oct 23 2019 RDO <dev@lists.rdoproject.org> 0.8.0-1.a09f5ddgit
- Update to 0.8.0

* Thu Oct 17 2019 RDO <dev@lists.rdoproject.org> 0.7.2-2.a09f5dd7git
- Update to post 0.7.2 (a09f5dd75bb0ee0605b013b2c604dd64e259e948)

