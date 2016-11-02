Name:           ros-kinetic-rqt-robot-steering
Version:        0.5.5
Release:        0%{?dist}
Summary:        ROS rqt_robot_steering package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_robot_steering
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-python-qt-binding >= 0.2.19
Requires:       ros-kinetic-rostopic
Requires:       ros-kinetic-rqt-gui
Requires:       ros-kinetic-rqt-gui-py
BuildRequires:  ros-kinetic-catkin

%description
rqt_robot_steering provides a GUI plugin for steering a robot using Twist
messages.

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
* Wed Nov 02 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.5-0
- Autogenerated by Bloom

* Mon Sep 19 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.4-0
- Autogenerated by Bloom

* Mon May 16 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.3-0
- Autogenerated by Bloom

* Fri Apr 29 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.2-1
- Autogenerated by Bloom

* Fri Apr 29 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.2-0
- Autogenerated by Bloom

* Thu Apr 28 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.1-0
- Autogenerated by Bloom

