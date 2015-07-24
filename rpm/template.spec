Name:           ros-jade-rqt-rviz
Version:        0.4.2
Release:        0%{?dist}
Summary:        ROS rqt_rviz package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_rviz
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-jade-pluginlib
Requires:       ros-jade-rqt-gui
Requires:       ros-jade-rqt-gui-cpp
Requires:       ros-jade-rviz
BuildRequires:  boost-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-pluginlib
BuildRequires:  ros-jade-rqt-gui
BuildRequires:  ros-jade-rqt-gui-cpp
BuildRequires:  ros-jade-rviz

%description
rqt_rviz provides a GUI plugin embedding RViz. Note that this rqt plugin does
NOT supersede RViz but depends on it.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Jul 24 2015 Aaron Blasdel <ablasdel@gmail.com> - 0.4.2-0
- Autogenerated by Bloom

* Thu Apr 30 2015 Aaron Blasdel <ablasdel@gmail.com> - 0.4.1-0
- Autogenerated by Bloom

