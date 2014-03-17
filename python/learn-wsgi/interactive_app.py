from paste.request import parse_formvars

def app(environ,start_response):
    fields = parse_formvars(environ)
    if environ['REQUEST_METHOD'] == 'POST':
        start_response('200 OK',[('content-type','text/html')])
        return ['Hello',fields['name'],'!']
    else:
        start_response('200 OK',[('content-type','text/html')])
        return ['<form method="POST">Name:<input type="text" '
                'name="name"><input type="submit"></form>']
        

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(app,host='127.0.0.1',port='8080')
