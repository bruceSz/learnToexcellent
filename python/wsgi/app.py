from webob import Response
from webob.dec import wsgify
from paste import httpserver
from paste.deploy import loadapp 

@wsgify
def app(req):
    return Response('Hello World')

def app_factory(global_config,**local_config):
    return app

def app_factory1(global_config,**local_config):
    return Response('no ,ha ha ')

wsgi_app = loadapp('config:/home/bruce/learnToexcellent/python/wsgi/paste.ini')
httpserver.serve(wsgi_app,'127.0.0.1',port=8080)

    

