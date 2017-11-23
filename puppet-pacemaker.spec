%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-pacemaker
%global commit 7403757dc6a29916c3907612c34b8f7b2557c347
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-pacemaker
Version:        0.5.0
Release:        2%{?alphatag}%{?dist}
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
* Wed May 17 2017 Michele Baldessari <michele@acksyn.org> 0.5.0-2.7403757dgit
- Ocata update 0.5.0 (7403757dc6a29916c3907612c34b8f7b2557c347)

* Mon Mar 06 2017 Alfredo Moralejo <amoralej@redhat.com> 0.5.0-1.fe4d4489git
- Ocata update 0.5.0 (fe4d448938b602a91ada9c66b14a76d38e740f12)

* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 0.4.0-1.28020degit
- Ocata update 0.4.0 (28020de0fb5699104057eed7a96d106bc396c9a2)

# REMOVEME: error caused by commit https://github.com/openstack/puppet-pacemaker/commit/1b7b9e99498dbdeaf722054d4d16a3b19e48d6ee
