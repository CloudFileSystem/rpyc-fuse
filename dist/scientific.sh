#!/bin/bash

#
# install python setuptools
#
sudo yum -y install python-setuptools
sudo yum -y install python-devel

#
# install FUSE
#
sudo yum -y install fuse fuse-devel

#
# install pip
#
easy_install pip

#
# install virtualenv
#
sudo pip install virtualenv

#
# activate virtualenv
#
virtualenv .
source ./bin/activate

#
# install virtualenv
#
pip install fuse-python
pip install fusepy

# vim: set nu ts=2 autoindent : #

