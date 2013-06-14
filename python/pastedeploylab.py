'''
created on 2013-06-14
copied from Sonic
'''
import os
import webob
from webob import Request
from webob import Response
from paste.deploy import loadapp
from wsgiref.simple_server import make_server

#Filter
class LogFilter():
	def __init__(self,app):
		self.app = app
		pass

	def __call__(self,environ,start_response):
		print 'filter:LogFilter is called'
		return self.app(environ,start_response)
	
	@classmethod
	def factory(cls,global_conf,**kwargs):
		print 'in LogFilter.factory',global_conf,kwargs
		return LogFilter
	
#app:ShowVersion
class ShowVersion():
	def __init__(self):
		pass

	def __call__(self,environ,start_response):
		start_response('200 OK',[("Content-Type","text/plain")])
		return ['paste deploy lab:version = 1.0.0',]
	
	@classmethod
	def factory(cls,global_conf,**kwargs):
		print 'in show version.factory',global_conf,kwargs
		return ShowVersion()

#app:Calculator
class Calculator():
	def __init__(self):
		pass
	
	def __call__(self,environ,start_response):
		req = Request(environ)
		res = Response()
		res.status = "200 OK"
		res.content_type = "text/plain"
		
		operator = req.GET.get("operator",None)
		operand1 = req.GET.get("operand1",None)
		operand2 = req.GET.get("operand2",None)
		print req.GET
		opnd1 = int(operand1)
		opnd2 = int(operand2)
		if operator == u'plus':
			opnd1 = opnd1 + opnd2
		elif operator == u'minux':
			opnd1 = opnd1 - opdn2
		elif operator == u'start':
			opnd1 = opnd1 * opnd2
		elif operator == u'slash':
			opnd1 = opnd1 / opnd2
		res.body = "%s /nRESULT=%d"%(str(req.GET),opnd1)
		return res(environ,start_response)
	@classmethod
	def factory(cls,global_conf,**kwargs):
		print 'calculator.factory' ,global_conf,kwargs
		return Calculator

if __name__ == '__main__':
	configfile = "pastedeploylab.ini"
	appname="pdl"
	wsgi_app = loadapp("config:%s"%os.path.abspath(configfile),appname)
	server = make_server('localhost',8080,wsgi_app)
	server.serve_forever()
	pass
			
