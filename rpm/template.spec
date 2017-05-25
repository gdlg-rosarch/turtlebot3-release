Name:           ros-kinetic-turtlebot3-navigation
Version:        0.1.5
Release:        0%{?dist}
Summary:        ROS turtlebot3_navigation package

Group:          Development/Libraries
License:        Apache License 2.0
URL:            http://turtlebot3.robotis.com
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-amcl
Requires:       ros-kinetic-map-server
Requires:       ros-kinetic-move-base
BuildRequires:  ros-kinetic-amcl
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-map-server
BuildRequires:  ros-kinetic-move-base

%description
The turtlebot3_navigation package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu May 25 2017 Pyo <pyo@robotis.com> - 0.1.5-0
- Autogenerated by Bloom

* Tue May 23 2017 Pyo <pyo@robotis.com> - 0.1.4-0
- Autogenerated by Bloom

* Mon Apr 24 2017 Pyo <pyo@robotis.com> - 0.1.3-0
- Autogenerated by Bloom

