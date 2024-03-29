Name:		xbiff
Version:	1.0.5
Release:	1
Summary:	Mailbox flag for X
Group:		Development/X11
Url:      https://gitlab.freedesktop.org/xorg/app/xbiff
Source:		https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT

BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	xaw-devel >= 1.0.1
BuildRequires:	pkgconfig(xbitmaps) >= 1.0.1
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1

%description
The xbiff program displays a little image of a mailbox. When there is no mail,
the flag on the mailbox is down. When mail arrives, the flag goes up and the
mailbox beeps.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xbiff
%{_mandir}/man1/xbiff.*
