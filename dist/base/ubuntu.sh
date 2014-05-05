#!/bin/bash

#
# install python setuptools
#
sudo apt-get -y install python-setuptools
sudo apt-get -y install python-pip
sudo apt-get -y install python-dev

#
# install FUSE
#
sudo apt-get -y install fuse
sudo apt-get -y install libfuse-dev

#
# install pip
#
easy_install pip

#
# install virtualenv
#
sudo pip install virtualenv

# vim: set nu ts=2 autoindent : #

