from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('shout', api.shout),
    url('whisper', api.whisper),
    url('get_item', api.get_item),
    url('drop_item', api.drop_item),
    url('pusher_auth', api.pusher_auth),
]
