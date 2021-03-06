Name:           gstreamer0.10-jolla
Summary:        Collection of Jolla specific GStreamer plugins
Version:        1.0.0
Release:        1
Group:          Applications/Multimedia
License:        LGPLv2.1
URL:            http://jollamobile.com
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(gstreamer-video-0.10)
BuildRequires:  pkgconfig(android-headers)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libhardware)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(nemo-gstreamer-interfaces-0.10)

%description
Collection of Jolla specific GStreamer plugins

%package -n libgstreamer0.10-nativebuffer
Summary: gstreamer native buffer library
Group: Applications/Multimedia
%description -n libgstreamer0.10-nativebuffer
%{summary}
%post -n libgstreamer0.10-nativebuffer -p /sbin/ldconfig
%postun -n libgstreamer0.10-nativebuffer -p /sbin/ldconfig

%package -n libgstreamer0.10-nativebuffer-devel
Summary: gstreamer native buffer library devel package
Group: Applications/Multimedia
Requires: libgstreamer0.10-nativebuffer = %{version}-%{release}
%description -n libgstreamer0.10-nativebuffer-devel
%{summary}
%post -n libgstreamer0.10-nativebuffer-devel -p /sbin/ldconfig
%postun -n libgstreamer0.10-nativebuffer-devel -p /sbin/ldconfig

%package -n libgstreamer0.10-gralloc
Summary: gstreamer gralloc library
Group: Applications/Multimedia
%description -n libgstreamer0.10-gralloc
%{summary}
%post -n libgstreamer0.10-gralloc -p /sbin/ldconfig
%postun -n libgstreamer0.10-gralloc -p /sbin/ldconfig

%package -n libgstreamer0.10-gralloc-devel
Summary: gstreamer gralloc library devel package
Group: Applications/Multimedia
Requires: libgstreamer0.10-gralloc = %{version}-%{release}
%description -n libgstreamer0.10-gralloc-devel
%{summary}
%post -n libgstreamer0.10-gralloc-devel -p /sbin/ldconfig
%postun -n libgstreamer0.10-gralloc-devel -p /sbin/ldconfig

%package -n gstreamer0.10-droideglsink
Summary: droideglsink HW accelerated sink
Group: Applications/Multimedia
%description -n gstreamer0.10-droideglsink
%{summary}

%prep
%setup -q

%build
%autogen
%configure
make %{?jobs:-j%jobs}

%install 
%make_install
# codecbin is broken for now
rm %{buildroot}/%{_libdir}/gstreamer-0.10/libgstcodecbin.so

%files -n libgstreamer0.10-nativebuffer
%defattr(-,root,root,-)
%{_libdir}/libgstnativebuffer.so.*

%files -n libgstreamer0.10-nativebuffer-devel
%defattr(-,root,root,-)
%{_libdir}/libgstnativebuffer.so
%{_libdir}/pkgconfig/libgstnativebuffer.pc
%{_includedir}/gstreamer-0.10/gst/gstnativebuffer.h

%files -n libgstreamer0.10-gralloc
%defattr(-,root,root,-)
%{_libdir}/libgstgralloc.so.*

%files -n libgstreamer0.10-gralloc-devel
%defattr(-,root,root,-)
%{_libdir}/libgstgralloc.so
%{_libdir}/pkgconfig/libgstgralloc.pc
%{_includedir}/gstreamer-0.10/gst/gstgralloc.h

%files -n gstreamer0.10-droideglsink
%defattr(-,root,root,-)
%{_libdir}/gstreamer-0.10/libgstdroideglsink.so
