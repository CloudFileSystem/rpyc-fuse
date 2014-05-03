#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rpyc
from rpyc.utils.server import ThreadedServer

class RPYCFuseService(rpyc.Service):
 	def on_connect(self):
		# code that runs when a connection is created
		# (to init the serivce, if needed)
		print "Server Connection OK!!"
 
	def exposed_printf(self, msg):
		return msg
 
	def on_disconnect(self):
		# code that runs when the connection has already closed
		# (to finalize the service, if needed)
		print "Server DISConnection!!"

if __name__ == "__main__":
	thread = ThreadedServer(RPYCFuseService, port=11025)
	thread.start()

