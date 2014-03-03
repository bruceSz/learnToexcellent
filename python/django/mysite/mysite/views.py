import datetime

from django.http import HttpResponse



def hello(request):
    return HttpResponse("hello world")

def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" %now
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body><html>." %(offset,dt)
    return HttpResponse(html)



