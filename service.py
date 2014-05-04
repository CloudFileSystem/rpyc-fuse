#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import rpyc
from rpyc.utils.server import ThreadedServer

class RPYCFuseService(rpyc.Service):
	def getpath(self, path):
		return '/home/naoya/Desktop/rpyc-fuse/srv' + path

	def on_connect(self):
		# code that runs when a connection is created
		# (to init the serivce, if needed)
		print "Server Connection OK!!"
 
	def exposed_open(self, path, flags, mode):
		print "OPEN"
		full_path = self.getpath(path)
		return os.open(full_path, flags)

	def exposed_read(self, path, length, offset, fh):
		print "READ"
		os.lseek(fh, offset, os.SEEK_SET)
		return os.read(fh, length)

	def exposed_write(self, path, buf, offset, fh):
		print "WRITE"
		os.lseek(fh, offset, os.SEEK_SET)
		return os.write(fh, buf)

	def exposed_flush(self, path, fh):
		print "FLSUH"
		return os.close(fh)

	def exposed_unlink(self, path):
		print "UNLINK"
		return os.unlink(self.getpath(path))

	def exposed_access(self, path, mode):
		full_path = self.getpath(path)
		return os.access(full_path, mode)

	def exposed_rmdir(self, path):
		full_path = self.getpath(path)
		return os.rmdir(full_path)

	def exposed_mkdir(self, path, mode):
		return os.mkdir(self.getpath(path), mode)

	def exposed_readdir(self, path, fh):
		return ['.', '..'] + os.listdir(self.getpath(path))

	def exposed_getattr(self, path, fh=None):
		st = os.lstat(self.getpath(path))
		return dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
		'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid'))
 
	def on_disconnect(self):
		# code that runs when the connection has already closed
		# (to finalize the service, if needed)
		print "Server DISConnection!!"

if __name__ == "__main__":
	thread = ThreadedServer(RPYCFuseService, port=11025, protocol_config={"allow_public_attrs":True})
	thread.start()

