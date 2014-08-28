from paste import loadapp

class ShowVersion(object):
    """
    app
    """
    def __init__(self,version):
        self.version = version

    def __call__(self,environ,start_response):
        res = Response()
        res.status = '200 OK'
        res.content_type = "text/plain"
        content = []
        content.append("%s\n",self.version)
        res.body = '\n'.join(content)
        return res(environ,start_response)

    @classmethod
    def factory(cls,global_conf,**kwargs):
        print 'factory'
        print 'kwargs:',kwargs
        return ShowVersion(kwargs['version'])

class LogFilter(object):
    


if __name__ == "__main__" :
    config = 'python_paste.ini'
    appname = 'common'
    wsgi_app = loadapp("config:%s"%os.path.abspath(config),appname)
    server = make_server('localhost',80,wsgi_app)
    server.serve_forever()
