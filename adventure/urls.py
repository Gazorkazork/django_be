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
<<<<<<< HEAD
    url('pusher_auth', api.pusher_auth),
=======
    url('look_item', api.look_item),
>>>>>>> 534789d778c7269f14427a95a55f4b5719e8a7e3
]
