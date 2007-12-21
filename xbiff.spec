Name:		xbiff
Version:	1.0.1
Release:	%mkrel 7
Summary:	Mailbox flag for X
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	libxext-devel >= 1.0.0
BuildRequires:	libxaw-devel >= 1.0.1
BuildRequires:	x11-data-bitmaps >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

%description
The xbiff program displays a little image of a mailbox. When there is no mail,
the flag on the mailbox is down. When mail arrives, the flag goes up and the
mailbox beeps.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -ifs
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xbiff
%{_mandir}/man1/xbiff.*


