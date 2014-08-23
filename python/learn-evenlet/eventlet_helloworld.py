from eventlet import wsgi
import eventlet

def hello_world(env,start_response):
    start_response('200 OK',[('Content-Type','text/plain')])
    return ['Hello,World!\n']

_sock = eventlet.listen(('',8090))
_pool = eventlet.GreenPool(1000)
_gt = eventlet.spawn(wsgi.server,
                        sock=_sock,
                        site=hello_world,
                        protocol=eventlet.wsgi.HttpProtocol,
                        custom_pool=_pool)

