%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-pacemaker
%global commit 87968ef1e717a33dd959ed089978b1abe9ca3e74
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-pacemaker
Version:        0.3.0
Release:        0.1%{?alphatag}%{?dist}
Summary:        Puppet module for Pacemaker
License:        Apache-2.0

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
* Fri Nov 04 2016 Jon Schlueter <jschluet@redhat.com> 0.3.0-0.1
- syncing version number with metadata.json

* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> - 0.0.1-0.1.87968ef.git
- Newton update 0.0.1 (87968ef1e717a33dd959ed089978b1abe9ca3e74)


