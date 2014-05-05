#!/bin/bash

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

