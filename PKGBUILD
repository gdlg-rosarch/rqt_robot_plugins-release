# Script generated with Bloom
pkgdesc="ROS - rqt_robot_monitor displays diagnostics_agg topics messages that are published by <a href="http://www.ros.org/wiki/diagnostic_aggregator">diagnostic_aggregator</a>. rqt_robot_monitor is a direct port to rqt of <a href="http://www.ros.org/wiki/robot_monitor">robot_monitor</a>. All diagnostics are fall into one of three tree panes depending on the status of diagnostics (normal, warning, error/stale). Status are shown in trees to represent their hierarchy. Worse status dominates the higher level status.<br/> <ul> Ex. 'Computer' category has 3 sub devices. 2 are green but 1 is error. Then 'Computer' becomes error. </ul> You can look at the detail of each status by double-clicking the tree nodes.<br/> Currently re-usable API to other pkgs are not explicitly provided."
url='http://ros.org/wiki/rqt_robot_monitor'

pkgname='ros-kinetic-rqt-robot-monitor'
pkgver='0.5.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('python2-rospkg'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-python-qt-binding>=0.2.19'
'ros-kinetic-qt-gui'
'ros-kinetic-qt-gui-py-common'
'ros-kinetic-rospy'
'ros-kinetic-rqt-bag'
'ros-kinetic-rqt-gui'
'ros-kinetic-rqt-gui-py'
'ros-kinetic-rqt-py-common'
)

conflicts=()
replaces=()

_dir=rqt_robot_monitor
source=()
md5sums=()

prepare() {
    cp -R $startdir/rqt_robot_monitor $srcdir/rqt_robot_monitor
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

