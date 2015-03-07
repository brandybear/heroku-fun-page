from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url="/polls/", permanent =False), name="index"),
    url(r'^polls/', include('polls.urls', namespace = 'polls')),
    url(r'^admin/', include(admin.site.urls)),
)
