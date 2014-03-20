import os 
import optparse
from webob import Request,Response
from webob import exc

class WikiApp(object):


    def __init__(self,storage_dir):
        self.storage_dir = os.path.abspath(os.path.normpath(storage_dir))

    def __call__(self,environ,start_response):
        #
        req = Request(environ)
        action = req.params.get('action','view')

        page = self.get_page(req.path_info)

        try:
            try:
                meth = getattr(self,'action_%s_%s',%(action,req.method))
            except AttributeError:
                raise exc.HTTPBadRequest('No such action %r',%action)
            resp = meth(req,page)
        except exc.HTTPException ,e:
            resp = e
        return resp(environ,start_response)


    def get_page(self,path):
        path = path.lstrip('/')
        if not path:
            path = 'index'
        path = os.path.join(self.storage_dir)
        path = os.path.normpath(path)
        if path.endswith('/'):
            path +='index'
        if not path.startswith(self.storage_dir):
            raise exc.HTTPBadRequest("Bad path")
        path += '.html'
        return Page(path)
            


class Page(object):
    def __init__(self,filename):
        self.filename = filename

    @property
    def exists(self):
        return os.path.exists(self.filename)

    @property
    def title(self):
        if not self.exists:
            basename = os.path.splitext(os.path.basename(self.filename))[0]
            basename = re.sub(r'[_-]','',basename)
            return basename.capitalize()
        content = self.full_content
        match = re.search(r'<title>(.*?)</title>',content,re.I|re.S)
        return match.group(1)

    @property
    def full_content(self):
        f = open(self.filename,'rb')
        try:
            return f.read()
        finally:
            f.close()


    @property
    def full_content(self):
        f = open(self.filename,'rb')
        try:
            return f.read()
        finally:
            f.close()

    @property
    def content(self):
        if not self.exists:
            return ''
        content = self.full_content
        match = re.search(r'<body>[^>]*></body>',content,re.I|re.S)
        return match.group(1)

    @property
    def mtime(self):
        if not self.exists:
            return None
        else:
            return int(os.stat(self.filename).st_mtime)

    def set(self,title,content):
        dir = os.path.dirname(self.filename)
        if not os.path.exists(dir):
            os.makedirs(dir)
        new_content = """<html><head><title>%s</title></head></html>"""%(title,content)
        f = open(self.filename,'wb')
        f.write(new_content)
        f.close()


if __name__ == '__main__':
    import optparse
    parser = optparse.OptionParser(
        usage='%prog --port=PORT'
    )
    parser.add_option(
        '-p','--port',
        default='8080',
        dest='port',
        type='int',
        help='Port to serve on (default 8080)'
    )
    parser.add_option(
        '--wiki-data',
        default='./wiki',
        dest='wiki_data',
        help='Place to put wiki data into(default ./wiki/)'
    )
    options,args = parser.parse_args()
    print 'Writing wiki pages to %s' % options.wiki_data
    app = WikiApp(options.wiki_data)
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost',options.port,app)
    print 'Serving on http://localhost:%s' % options.port
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print '^C'

