from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import Hello

urlpatterns = patterns('',
    url(r'^$',Hello.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
