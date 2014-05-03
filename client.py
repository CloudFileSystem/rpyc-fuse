#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rpyc
from fuse import FUSE, FuseOSError, Operations

class RPYCFuse(Operations):
	def __init__(self):
		#client = rpyc.connect("localhost", 11025)
		#client.root
		#print client.root.Main.printf("Hello world!!")
		pass
 
	# +============================
	# | Filesystem method
	# +============================
	def access(self, path, mode):
		raise FuseOSError(errno.EACCES)
 
	def chmod(self, path, mode):
		raise FuseOSError(errno.EACCES)
 
	def chown(self, path, mode):
		raise FuseOSError(errno.EACCES)
 
	def getattr(self, path, fh=None):
		raise FuseOSError(errno.EACCES)
 
	def getxattr(self, path, fh=None):
		raise FuseOSError(errno.EACCES)
 
	def readdir(self, path, fh):
		raise FuseOSError(errno.EACCES)
		#return ['.', '..'] + os.listdir(path)
 
	def readlink(self, path):
		raise FuseOSError(errno.EACCES)
 
	def mknod(self, path, mode, dev):
		raise FuseOSError(errno.EACCES)
 
	def mkdir(self, path, mode):
		raise FuseOSError(errno.EACCES)
 
	def rmdir(self, path):
		raise FuseOSError(errno.EACCES)
 
	def statfs(self, path):
		raise FuseOSError(errno.EACCES)
 
	def unlink(self, path):
		raise FuseOSError(errno.EACCES)
 
	def symlink(self, target, source):
		raise FuseOSError(errno.EACCES)
 
	def rename(self, old, new):
		raise FuseOSError(errno.EACCES)
 
	def link(self, target, source):
		raise FuseOSError(errno.EACCES)
 
	def utimens(self, path, times=None):
		raise FuseOSError(errno.EACCES)
 
	# +============================
	# | File method
	# +============================
	def open(self, path, flags):
		raise FuseOSError(errno.EACCES)
 
	def create(self, path, mode):
		raise FuseOSError(errno.EACCES)
 
	def read(self, path, size, offset, fh):
		raise FuseOSError(errno.EACCES)
 
	def write(self, path, data, offset, fh):
		raise FuseOSError(errno.EACCES)
 
	def truncate(self, path, length, fh=None):
		raise FuseOSError(errno.EACCES)
 
	def flush(self, path, fh):
		raise FuseOSError(errno.EACCES)
 
	def release(self, path, fh):
		raise FuseOSError(errno.EACCES)
 
	def fsync(self, path, datasync, fh):
		raise FuseOSError(errno.EACCES)

if __name__ == "__main__":
	FUSE(RPYCFuse(), './mnt', noempty=True)

