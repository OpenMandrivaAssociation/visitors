Summary:	Process a web log file for visitor statistics
Name:		visitors
Version:	1.1
Release:	%mkrel 1
License:	GPL
Group:		File tools
URL:		http://www.stedee.id.au/visitors
Source:		http://www.stedee.id.au/files/%{name}-%{version}.tar.bz2
BuildRequires:	db4-devel
BuildRequires:	pcre-devel
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
visitors processes a web log file trying very hard to identify a single
"person" as much as possible. This is typically achieved by use of either an
identifying cookie in the log file; Or via the IP Address/Name & Browser ID
combination.

%prep

%setup -q

%build

%configure2_5x \
    --enable-database-name=%{name}.db \
    --enable-database-dir=%{_localstatedir}/lib/%{name}
	
%make

%install
rm -rf %{buildroot}

%makeinstall

install -d %{buildroot}%{_localstatedir}/lib/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc ChangeLog COPYING INSTALL README
%{_bindir}/%{name}
%dir %{_localstatedir}/lib/%{name}
%{_mandir}/man1/%{name}.1*


