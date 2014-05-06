#!/bin/bash

#
# activate virtualenv
#
virtualenv .
source ./bin/activate

#
# install fuse binding
#
pip install fuse-python
pip install fusepy

#
# install rpyc
#
pip install rpyc

#
# install cython
#
vpath="`which virtualenv`/"
pip install --install-option="--prefix=$vpath" cython

# vim: set nu ts=2 autoindent : #

