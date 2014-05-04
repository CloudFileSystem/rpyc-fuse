#!/usr/bin/env python
# -*- coding: utf-8 -*-
import errno
import os
import os.path

import rpyc
from fuse import FUSE, FuseOSError, Operations

class RPYCFuse(Operations):
	def __init__(self):
		#self.client = rpyc.connect("localhost", 11025)
		self.client = rpyc.connect("10.3.1.40", 11025)

	# +============================
	# | Filesystem method
	# +============================
	def access(self, path, mode):
		result = self.client.root.access(path, mode)
		return result

	chmod		= None
	chown		= None
	def getattr(self, path, fh=None):
		result = self.client.root.getattr(path, fh)
		return result

	getxattr	= None

	def readdir(self, path, fh):
		result = self.client.root.readdir(path, fh)
		return result

	readlink	= None
	mknod		= None

	def rmdir(self, path):
		return self.client.root.rmdir(path)

	def unlink(self, path):
		return self.client.root.unlink(path)

	def mkdir(self, path, mode):
		result = self.client.root.mkdir(path, mode)
		return result

	statfs		= None
	symlink		= None
	rename		= None
	link		= None
	def utimens(self, path, times=None):
		return None
 
	# +============================
	# | File method
	# +============================
	def open(self, path, flags, mode=None):
		return self.client.root.open(path, flags, mode)

	def create(self, path, mode):
		return self.open(path, os.O_WRONLY | os.O_CREAT, mode)

	def read(self, path, length, offset, fh):
		return self.client.root.read(path, length, offset, fh)

	def write(self, path, buf, offset, fh):
		return self.client.root.write(path, buf, offset, fh)

	truncate	= None

	def flush(self, path, fh):
		return self.client.root.flush(path, fh)

	release		= None
	fsync		= None

if __name__ == "__main__":
	mntpoint = os.path.abspath('%s/mnt' %(os.path.dirname(os.path.abspath(__file__))))
        print "I will mount %s" %(mntpoint)
        FUSE(RPYCFuse(), mntpoint, foreground=True, nonempty=True, allow_other=True)

