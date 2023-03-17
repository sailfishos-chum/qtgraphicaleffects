%global qt_version 5.15.8

Summary: Qt5 - QtGraphicalEffects component
Name: opt-qt5-qtgraphicaleffects
Version: 5.15.8
Release: 1%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively from qt5-qtbase for details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io
Source0: %{name}-%{version}.tar.bz2

# filter qml provides
%global __provides_exclude_from ^%{_opt_qt5_archdatadir}/qml/.*\\.so$

BuildRequires: make
BuildRequires: opt-qt5-qtbase-devel >= %{qt_version}
BuildRequires: opt-qt5-qtbase-private-devel
#libQt5Quick.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtdeclarative
BuildRequires: opt-qt5-qtdeclarative-devel

BuildRequires: pkgconfig(libmng)
BuildRequires: pkgconfig(libtiff-4)

%description
The Qt Graphical Effects module provides a set of QML types for adding
visually impressive and configurable effects to user interfaces. Effects
are visual items that can be added to Qt Quick user interface as UI
components.


%prep
%autosetup -n %{name}-%{version}/upstream


%build
%{opt_qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}


%files
%license LICENSE.*
%{_opt_qt5_qmldir}/QtGraphicalEffects/
