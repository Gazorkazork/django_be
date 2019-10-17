from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json
import datetime

# instantiate pusher
pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config(
    'PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))


@csrf_exempt
@api_view(['POST'])
def pusher_auth(request):
    auth = pusher.authenticate(
        channel=request.form['presence-main-channel'],
        socket_id=request.form['socket_id']
    )
    return json.dumps(auth)
