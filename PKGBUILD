# Script generated with Bloom
pkgdesc="ROS - Metapackage of rqt plugins that are particularly used with robots during its operation.<br/> <br/> To run any rqt plugins, just type in a single command &quot;rqt&quot;, then select any plugins you want from the GUI that launches afterwards.<br/> <br/> rqt consists of three following metapackages:<br/> <ul> <li><a href="http://ros.org/wiki/rqt">rqt</a> - provides a container window where all rqt tools can be docked at. rqt plugin developers barely needs to pay attention.</li> <li><a href="http://ros.org/wiki/rqt_common_plugins">rqt_common_plugins</a> - ROS backend tools suite that can be used on/off of robot runtime.</li> <li>rqt_robot_plugins (You're here!)</li> </ul>"
url='http://ros.org/wiki/rqt_robot_plugins'

pkgname='ros-lunar-rqt-robot-plugins'
pkgver='0.5.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-rqt-moveit'
'ros-lunar-rqt-nav-view'
'ros-lunar-rqt-pose-view'
'ros-lunar-rqt-robot-dashboard'
'ros-lunar-rqt-robot-monitor'
'ros-lunar-rqt-robot-steering'
'ros-lunar-rqt-runtime-monitor'
'ros-lunar-rqt-rviz'
'ros-lunar-rqt-tf-tree'
)

conflicts=()
replaces=()

_dir=rqt_robot_plugins
source=()
md5sums=()

prepare() {
    cp -R $startdir/rqt_robot_plugins $srcdir/rqt_robot_plugins
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

