import datetime

from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render




def hello(request):
    return HttpResponse("hello world")

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
    return HttpResponse('<table>%s</table>' %  '\n'.join(html))

def current_time(request):
    now = datetime.datetime.now()
    # 1 :below is the simplest way to uilize the template.
        # t = Template("<html><body>It is now {{current_date}}.</body><html>")

    # 2 :below is a better way to utilize the template
        # fp = open('/tmp/templates/mytemplate.html')
        # t = Template(fp.read())

        # fp.close()
    # 3 :Using get_template.
        # t = get_template('current_datetime.html')
        # html = t.render(Context({'current_date':now}))
    # render shortcut.
    return render(request,'current_datetime.html',{'current_date':now})
    

    #html = "<html><body>It is now %s.</body></html>" %now
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body><html>." %(offset,dt)
    return HttpResponse(html)



def book_list(request):
    
    # simple and foolish
        # db = MySQL.connect(user= 'test',db='test',passwd='123456',host='localhost')
        # cursor = db.cursor()
        # cursor.execute('SELECT NAME from books order by name')
        # names = [row[0] for row in cursor.fetchall()]
        # db.close()
        # return render(request,'book_list.html',{'names':names})
    books = Book.objects.order_by('name')
    return render(request,'book_list.html',{'books':books})

