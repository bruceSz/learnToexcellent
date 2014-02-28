import datetime

from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello world")

def current_time(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{current_date}}.</body><html>")
    html = t.render(Context('current_date':now))

    #html = "<html><body>It is now %s.</body></html>" %now
    return HttpResponse(html)



