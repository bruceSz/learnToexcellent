class ObjectPublisher(object):

    def __init__(self,root):
        self.root = root

    def __call__(self,environ,start_response):
        fields = parse_formvars(environ)
        obj = self.find_object(self.root,environ)
        response_body = obj(**fields.mixed())
        start_response('200 OK',[('content-type','text/html')])
        return [response_body]

    def find_object(self,obj,environ):
        path_info = environ.get('PATH_INFO','')
        if not path_info or path_info == '/':
            return obj
        path_info = path_info.lstrip('/')
        parts = path_info.split('/',1)
        next = parts[0]
        if len(parts) == 1:
            rest = ''
        else:
            rest = '/'+parts[1]

        assert not next.startswith('_')

        next_obj = getattr(obj,next)

        environ['SCRIPT_NAME'] +='/' + next
        environ['PATH_INFO'] = rest

        return self.find_objects(next_obj,environ)

class Root(object):
    def __call__(self):
        return '''
        <form action="welcome">
            Name:<input type="text" name="name">
            <input type="submit">
        </form>
        '''

    def welcome(self,name):
        return " Hello %s!" % name

app = ObjectPublisher(Root())


if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(app,host='127.0.0.1',port='8080')
