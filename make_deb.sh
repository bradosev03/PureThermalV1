#!/bin/bash

dir=`pwd`;
control="control";
appName="PureThermalV1-DEB";
folder="DEBIAN";
version="1.0.0"
name="thermalpi";
debname="${name}_${version}.deb"

cd ..;
mkdir -p "${appName}/${folder}";
mkdir -p "${appName}/usr/bin/";

cat <<EOF >"${appName}/${folder}/control"
Package: ${name}
Version: ${version}
Maintainer: bradosev03
Architecture: all
Depends: python, python-opencv, autotools-dev, autoconf, build-essential, libv4l-dev, v4l-utils
Description: thermalpi
  A Simple program written in Python2.7 that is used to capture 
  thermal images from multiple cameras concurrently. It outputs 
  the date to a folder under your user ~/thermalpi/images/ . It 
  utilizes OpenCV2 and the threading library built into Python.
  It can be run in both a visual mode, in which the data captured
  is displayed in a popup window as well as in its default configs
  of headless mode in which it just stores it data to 
  ~/thermalpi/images.
EOF

cp "${dir}/capture.py" "${appName}/usr/bin/thermalpi"
chmod +x "${appName}/usr/bin/thermalpi";

echo "Creating Debian File: ${debname}";

dpkg-deb -b ${appName} ${debname};
rm -rf ${appName};
