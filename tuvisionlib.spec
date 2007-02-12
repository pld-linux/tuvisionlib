Summary:	TUVision Image Processing Library
Summary(pl.UTF-8):   TUVision - biblioteka do przetwarzania obrazu
Name:		tuvisionlib
Version:	0.9
Release:	1
License:	LGPL v2+ (see COPYING for exceptions)
Group:		Libraries
Source0:	http://www.ti1.tu-harburg.de/Lehre/software/tuvisionlib/%{name}-%{version}.tar.gz
# Source0-md5:	17be8ccf9e2950e6c1ea18e681c0ff4b
Patch0:		%{name}-opt.patch
URL:		http://www.ti1.tu-harburg.de/Lehre/software/tuvisionlib/main.html
BuildRequires:	jasper-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This C++ library is still under development as new algorithms will be
integrated over time, but it is already suitable for some tasks:

- representation of grayscale, RGB and YUV images based on the
  following datatypes: Byte, Int and Double
- file I/O: JPEG (r/w), TIFF (r/w), PGM (w), PNG and Gnuplot (w)
- basic filter types, generic convolution
- conversion of different bases
- edge detection, object extraction
- camera calibration, 3D coordinate transformations
- FFT of gray images

%description -l de.UTF-8
Die C++ - Bibliothek ist konstant im Entwicklungsstadium. Für viele
Anwendungen kann sie jedoch jetzt verwendet werden:

- Repräsentation von Grau-, RGB und YUV-Bildern mit den folgenden
  Datentypen: Byte, Int and Double
- Datei-I/O: JPEG (r/w), TIFF (r/w), PGM (w), PNG and Gnuplot (w)
- Grundlegende Filtertypen, generische Faltung
- Konvertierung verschiedener Datentypen
- Kantenerkennung, Objektextraktion
- Kamerakalibration, 3D-Koordinatentransformation
- FFT von Graubildern

%description -l pl.UTF-8
Ta biblioteka C++ jest ciągle rozwijana i w miarę upływu czasu będą
dodawane nowe algorytmy; jednak już teraz nadaje się do niektórych
zadań:

- reprezentowania obrazów w odcieniach szarości, RGB i YUV w oparciu o
  typy danych Byte, Int i Double
- operacji wejścia/wyjścia na plikach: JPEG (odczyt/zapis), TIFF
  (odczyt/zapis), PGM (zapis), PNG i Gnuplot (zapis)
- podstawowych rodzajów filtrów, ogólnych przekształceń
- wykrywania krawędzi, wyciągania obiektów
- kalibracji aparatów, przekształceń współrzędnych 3D
- FFT obrazów w skali szarości

%package devel
Summary:	Header files for TUVision library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki TUVision
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	jasper-devel
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libstdc++-devel
Requires:	libtiff-devel

%description devel
Header files for TUVision library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki TUVision.

%package static
Summary:	Static TUVision library
Summary(pl.UTF-8):   Statyczna biblioteka TUVision
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static TUVision library.

%description static -l pl.UTF-8
Statyczna biblioteka TUVision.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libtuvision-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.{html,css,gif} doc/images/*.jpg
%attr(755,root,root) %{_bindir}/tuvision-config
%attr(755,root,root) %{_libdir}/libtuvision.so
%{_libdir}/libtuvision.la
%{_includedir}/tuvisionlib

%files static
%defattr(644,root,root,755)
%{_libdir}/libtuvision.a
