Name: glxcompmgr
# date -u +%Y%m%d
Version: 20080416
Release: %mkrel 2
Summary: glxcompmgr - OpenGL compositing manager
Group: Development/X11
# git-archive --format=tar --prefix=glxcompmgr/ master | bzip2 > glxcompmgr.tar.bz2
Source: glxcompmgr.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: GL-devel
BuildRequires: libGConf2-devel cairo-devel
BuildRequires: libxcomposite-devel libpng-devel libxfixes-devel libxdamage-devel

%description
glxcompmgr - OpenGL compositing manager

glxcompmgr is an OpenGL compositing manager that use GLX_MESA_render_texture
for binding redirected top-level windows to texture objects. It has a flexible
plug-in system and it is designed to run well on most graphics hardware. 

%prep
%setup -q -n %{name}

%build
sh autogen.sh

%configure

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/glxcompmgr
%{_includedir}/glxcomp/comp.h
%{_includedir}/glxcomp/region.h
%{_libdir}/glxcomp/libcube.a
%{_libdir}/glxcomp/libcube.la
%{_libdir}/glxcomp/libcube.so
%{_libdir}/glxcomp/libexpose.a
%{_libdir}/glxcomp/libexpose.la
%{_libdir}/glxcomp/libexpose.so
%{_libdir}/glxcomp/libfade.a
%{_libdir}/glxcomp/libfade.la
%{_libdir}/glxcomp/libfade.so
%{_libdir}/glxcomp/libgconf.a
%{_libdir}/glxcomp/libgconf.la
%{_libdir}/glxcomp/libgconf.so
%{_libdir}/glxcomp/librotate.a
%{_libdir}/glxcomp/librotate.la
%{_libdir}/glxcomp/librotate.so
%{_libdir}/glxcomp/libshadow.a
%{_libdir}/glxcomp/libshadow.la
%{_libdir}/glxcomp/libshadow.so
%{_libdir}/glxcomp/libwobbly.a
%{_libdir}/glxcomp/libwobbly.la
%{_libdir}/glxcomp/libwobbly.so
%{_libdir}/glxcomp/libzoom.a
%{_libdir}/glxcomp/libzoom.la
%{_libdir}/glxcomp/libzoom.so
%{_libdir}/pkgconfig/glxcomp.pc
%{_datadir}/glxcomp/background.png
%{_datadir}/glxcomp/window.png
