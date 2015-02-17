Name:		spacewalk-ipa-client
Version:	2.3.0
Release:	1%{?dist}
Summary:	Package allowing IPA enrollment via Spacewalk

Group:		Applications/System
License:	GPLv2
URL:		https://fedorahosted.org/spacewalk
Source0:	https://fedorahosted.org/releases/s/p/spacewalk/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:  python-devel
Requires:       rhnlib
Requires:       rhn-check
Requires:       rhn-setup
Requires:       ipa-client
%description
spacewalk-ipa-client contains client side functionality allowing IPA enrollment
via Spacewalk

%prep
%setup -q


%build
make -f Makefile.spacewalk-ipa-client


%install
rm -rf $RPM_BUILD_ROOT
make -f Makefile.spacewalk-ipa-client install PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%config  /etc/sysconfig/rhn/clientCaps.d/spacewalk-ipa-client
%{_datadir}/rhn/actions/ipa.*


%changelog
