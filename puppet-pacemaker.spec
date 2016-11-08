%{!?upstream_version: %global upstream_version %{version}}
%define upstream_name puppet-pacemaker

Name:           puppet-pacemaker
Version:        0.4.0
Release:        0.1%{?dist}
Summary:        Puppet module for Pacemaker
License:        Apache-2.0

URL:            https://github.com/redhat-openstack/puppet-pacemaker

Source0:        https://github.com/openstack/%{name}/archive/%{version}.tar.gz

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
* Mon Nov 14 2016 Alex Schultz <aschultz@redhat.com> 0.4.0-0.1
- First actual tag from upstream

* Fri Nov 04 2016 Jon Schlueter <jschluet@redhat.com> 0.3.0-0.1
- syncing version number with metadata.json

* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> - 0.0.1-0.1.87968ef.git
- Newton update 0.0.1 (87968ef1e717a33dd959ed089978b1abe9ca3e74)


