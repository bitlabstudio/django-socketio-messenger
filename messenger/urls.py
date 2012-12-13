from django.conf.urls import patterns, include, url

from messenger.views import broadcast_channel


urlpatterns = patterns('',
    url(r'^broadcast_channel/$', broadcast_channel, name='broadcast_channel'),
    url(r'^', include('django_socketio.urls')),
)
