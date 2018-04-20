# Script generated with Bloom
pkgdesc="ROS - rqt_tf_tree provides a GUI plugin for visualizing the ROS TF frame tree."
url='http://ros.org/wiki/rqt_tf_tree'

pkgname='ros-kinetic-rqt-tf-tree'
pkgver='0.5.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('python2-mock'
'ros-kinetic-catkin'
)

depends=('python2-rospkg'
'ros-kinetic-geometry-msgs'
'ros-kinetic-python-qt-binding>=0.2.19'
'ros-kinetic-qt-dotgraph'
'ros-kinetic-rospy'
'ros-kinetic-rqt-graph'
'ros-kinetic-rqt-gui'
'ros-kinetic-rqt-gui-py'
'ros-kinetic-tf2'
'ros-kinetic-tf2-msgs'
'ros-kinetic-tf2-ros'
)

conflicts=()
replaces=()

_dir=rqt_tf_tree
source=()
md5sums=()

prepare() {
    cp -R $startdir/rqt_tf_tree $srcdir/rqt_tf_tree
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

