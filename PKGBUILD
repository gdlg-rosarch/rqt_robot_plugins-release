# Script generated with Bloom
pkgdesc="ROS - rqt_robot_dashboard provides an infrastructure for building robot dashboard plugins in rqt."
url='http://ros.org/wiki/rqt_robot_dashboard'

pkgname='ros-kinetic-rqt-robot-dashboard'
pkgver='0.5.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-diagnostic-msgs'
'ros-kinetic-python-qt-binding>=0.2.19'
'ros-kinetic-qt-gui'
'ros-kinetic-rospy'
'ros-kinetic-rqt-console>=0.3.1'
'ros-kinetic-rqt-gui'
'ros-kinetic-rqt-gui-py'
'ros-kinetic-rqt-nav-view'
'ros-kinetic-rqt-robot-monitor'
)

conflicts=()
replaces=()

_dir=rqt_robot_dashboard
source=()
md5sums=()

prepare() {
    cp -R $startdir/rqt_robot_dashboard $srcdir/rqt_robot_dashboard
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

