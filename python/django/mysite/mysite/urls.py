from django.conf.urls import patterns, include, url
from mysite.views import hello
from mysite.views import current_time
from mysite.views import hours_ahead

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^time/$',current_time),
    url(r'^time/plus/(\d{1,2})',hours_ahead),
)
