from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^(/)?$', RedirectView.as_view(url='/chats/')),
     url(r'^chats/', include('chat.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
     url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'registration/logout.html'}),
)
