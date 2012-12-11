Summary:	Process a web log file for visitor statistics
Name:		visitors
Version:	1.1
Release:	9
License:	GPL
Group:		File tools
URL:		http://www.stedee.id.au/visitors
Source:		http://www.stedee.id.au/files/%{name}-%{version}.tar.bz2
BuildRequires:	db-devel
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




%changelog
* Tue May 08 2012 Crispin Boylan <crisb@mandriva.org> 1.1-9
+ Revision: 797438
- Rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - relink against libpcre.so.1

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-7mdv2011.0
+ Revision: 615412
- the mass rebuild of 2010.1 packages

* Thu Dec 31 2009 Funda Wang <fwang@mandriva.org> 1.1-6mdv2010.1
+ Revision: 484301
- rebuild for db 4.8

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.1-5mdv2010.0
+ Revision: 434677
- rebuild
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.1-3mdv2009.0
+ Revision: 255563
- rebuild

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.1-1mdv2008.1
+ Revision: 129181
- kill re-definition of %%buildroot on Pixel's request

