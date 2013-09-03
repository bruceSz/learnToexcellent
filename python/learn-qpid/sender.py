#!/usr/bin/python
import qpid.messaging
from datetime import datetime
from base import QPIDBase

class QPIDSender(QPIDBase):
	def __init__(self,**kwargs):
		super(QPIDSender,self).__init__(**kwargs)
		self.sender = None
	
	def init_sender(self):
		"""initial the sender """
		if not self.session:
			self.init_session()
		self.sender = self.session.sender(self.queue_name)
			
	def send(self,content,t = 'test'):
		"""sending the content """
		if not self.sender:
			self.init_sender()
		props = {'type':t}
		message = qpid.messaging.Message(properties=props,content=content)
		self.sender.send(message)

	def typing(self):
		""" sending the contents real time with typing"""
		content = ''
		while content != 'EOF':
			content = raw_input('start typing:')
			self.send(content)

if __name__ == '__main__':
	s = QPIDSender()
	s.send('Testing at %s' %datetime.now())
	s.close()

