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
        resp = Response(
            'Hello %s!' %req.params.get('name','World'))
        return resp(environ,start_response)


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

