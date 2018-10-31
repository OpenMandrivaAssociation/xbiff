Name:		xbiff
Version:	1.0.3
Release:	14
Summary:	Mailbox flag for X
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: pkgconfig(xext) >= 1.0.0
BuildRequires: xaw-devel >= 1.0.1
BuildRequires: x11-data-bitmaps >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.0.1

%description
The xbiff program displays a little image of a mailbox. When there is no mail,
the flag on the mailbox is down. When mail arrives, the flag goes up and the
mailbox beeps.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%{_bindir}/xbiff
%{_mandir}/man1/xbiff.*
