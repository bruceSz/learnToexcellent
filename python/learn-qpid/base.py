#!/usr/bin/python

import qpid
import qpid.messaging
import logging
logging.basicConfig()

class QPIDBase(object):
	def __init__(self,host='127.0.0.1',port='5672',queue_name='hello',username='guest',password='guest'):
		"""
		arguments:
			host
			port
			queue_name
			username
			password

		"""
		self.host = host
		self.port = port
		self.queue_name = queue_name
		self.username = username
		self.password = password
		self.connection = None
		self.session = None
		
	def init_connection(self,mechanism='PLAIN'):
		""" initial the connection"""
		url = 'amqp://guest/guest@%s:%s' %(self.host,self.port)
		self.connection = qpid.messaging.Connection(url=url,sasl_mechanisms=mechanism,
													reconnect=True,reconnect_interval=60,
													reconnect_limit=60,username=self.username,password=self.password)
		self.connection.open()

	def init_session(self):
		""" initial the session"""
		if not self.connection:
			self.init_connection()
		self.session = self.connection.session()
	
	def close(self):
		"""close the connection and session"""
		self.session.close()
		self.connection.close()
