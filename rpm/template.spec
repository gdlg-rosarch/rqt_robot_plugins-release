Name:           ros-kinetic-rqt-robot-dashboard
Version:        0.5.2
Release:        1%{?dist}
Summary:        ROS rqt_robot_dashboard package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_robot_dashboard
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-python-qt-binding >= 0.2.19
Requires:       ros-kinetic-qt-gui
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rqt-console >= 0.3.1
Requires:       ros-kinetic-rqt-gui
Requires:       ros-kinetic-rqt-gui-py
Requires:       ros-kinetic-rqt-nav-view
Requires:       ros-kinetic-rqt-robot-monitor
BuildRequires:  ros-kinetic-catkin

%description
rqt_robot_dashboard provides an infrastructure for building robot dashboard
plugins in rqt.

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
* Fri Apr 29 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.2-1
- Autogenerated by Bloom

* Fri Apr 29 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.2-0
- Autogenerated by Bloom

* Thu Apr 28 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.1-0
- Autogenerated by Bloom

