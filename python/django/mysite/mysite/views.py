import datetime

from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello world")

def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" %now
    return HttpResponse(html)



