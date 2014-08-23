class route(object):
    def __init__(self,res):
        self.resource = res

    @classmethod
    def factory(cls):
        print 'factory'
        return cls()

    @webob.dec.wsgify
    def __call__(self,req):
        print 'route __call__'
        return self.resource()


class resource(object):
    
    @webob.dec.wsgify
    def __call__(self,req):
        print 'resource __call__'

class API(route):
    def __init__(self):
        res = resource()
        super(API,self).__init__(res)


wsgi.server(eventlet.listen(('',80)),API.factory())
