import logging
import os
import webob.dec
import webob.exc

from paste.deploy import loadapp
from wsgiref.simple_server import make_server

import routes.middleware

CONTEXT_ENV = 'openstack.context'
PARAMS_ENV = 'openstack.params'

LOG = logging.getLogger(__name__)

class Controller(object):
    @webob.dec.wsgify
    def __call__(self,req):
        arg_dict = req.environ['wsgiorg.routing_args'][1]
        action = arg_dict.pop('action')
        del arg_dict['controller']

        context = req.environ.get(CONTEXT_ENV,{})
        context['query_string'] = dict(req.params.iteritems())
        context['headers'] = dict(req.headers.iteritems())
        context['path'] = req.environ['PATH_INFO']
        params = req.environ.get(PARAMS_ENV,{})

        for name in ['REMOTE_USER','AUTH_TYPE']:
            try:
                context[name] = req.environ[name]
            except KeyError:
                try:
                    del context[name]
                except KeyError:
                    pass

        params.update(arg_dict)

        method = getattr(self,action)

        result = method(context,**params)
        return webob.Response('OK')

    def getMessage(self,context,user_id):
        return {'Message': 'TestMessage'}
        pass

class Router(object):
    def __init__(self):
        self._mapper = routes.Mapper()
        self._mapper.connect('/test/{user_id}',
                            controller=Controller(),
                            action='getMessage',
                            conditions={'method':['GET']}) 
        
        print 'router begin to be created.'
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,self._mapper)

    @webob.dec.wsgify
    def __call__(self,req):
        return self._router

    @staticmethod
    @webob.dec.wsgify
    def _dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        print 'routing to : ',req.environ['wsgiorg.routing_args']

        if not match:
            return webob.exc.HTTPNotFound()
        app = match['controller']
        return app

    @classmethod
    def app_factory(cls,global_config,**local_config):
        return cls()
        

if __name__ == '__main__':
    configfile = 'testroutes.ini'
    appname = "main"
    wsgi_app = loadapp("config:%s"%os.path.abspath(configfile),appname)
    print dir(wsgi_app)
    httpd = make_server('localhost',8282,wsgi_app)
    httpd.serve_forever()
