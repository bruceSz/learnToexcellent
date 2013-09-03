import sys
from qpid.messaging import *
import ConfigParser
class configuration():
	def __init__(self):
		self.cf = ConfigParser.ConfigParser()
		self.cf.read('test_qpid.conf')
	def __getattr__(self,key):
		if key == 'host':
			if not self.inner_host:
				self.inner_host = self.cf.get('DEFAULT','broker_host')
			return self.inner_host
		if key == 'port':
			if not self.inner_port:
				self.inner_port = self.cf.get('DEFAULT','broker_port')
			return self.inner_port
		if key == 'address':
			if not self.inner_address:
				self.inner_address = self.cf.get('DEFAULT','address')
			return self.inner_address
	
conf = configuration()
#from oslo.config import cfg

#DEBUG = False
#print 'config-debug-begin'
#opts = [
#	cfg.StrOpt('broker_host',default='127.0.0.1'),
#	cfg.StrOpt('address',default='hello'),
#	cfg.IntOpt('broker_port',default=5672),
#		]
#CONF = cfg.CONF
#CONF.register_opts(opts)
#
#print 'config-debug-end'

class test_method():

	def send(self,argv,session,address):
		sender = session.sender(address)
		sender.send(Message("hello world"))

	def receive_ack(self,argv,session,address):
		receiver = session.receiver(address)
		message = receiver.fetch(timeout=1)
		session.acknowledge()
		return message

	def receive(self,argv,session,address):
		receiver = session.receiver(address)
		message = receiver.fetch(timeout=1)
		return message

def test(argv):

	#CONF(default_config_files=["test_qpid.conf"])

	if len(argv) < 2:
		print "please input desired method "
		sys.exit()
		
	method_string = argv[1]
	print argv[1]

	t = test_method()
	method = getattr(t,method_string)

	connection = Connection(conf.host+':'+conf.port)
	try:
		connection.open()
		session = connection.session()
		ret = method(argv,session,conf.address)
		if ret:
			print ret
	except MessagingError,m:
		print m
	finally:
		connection.close()

if __name__ == '__main__':
	test(sys.argv)
