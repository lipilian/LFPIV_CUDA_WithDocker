#! /bin/bash

# update the apt-get
sudo apt-get update

# check version
lsb_release -a

# install dependence
sudo apt-get install python3-pyqt4
sudo apt-get install -y libfreeimage-dev
sudo apt-get install python3-opengl
sudo apt-get install python3-pyqt4.qtopengl
sudo apt-get install python3-numpy


