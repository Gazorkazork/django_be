from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json

# instantiate pusher
pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))


@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    planet_rooms = Room.objects.filter(planet=room.planet)
    planet_map = {
        "planet": room.planet,
        "rooms": [{
            'id': i.id,
            'x': i.coord_x,
            'y': i.coord_y,
            'north': i.north,
            'south': i.south,
            'east': i.east,
            'west': i.west
        } for i in planet_rooms]
    }
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'room_id': room.id, 'title':room.title, 'description':room.description, 'planet_map':planet_map, 'players':players}, safe=True)


@csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.north
    elif direction == "s":
        nextRoomID = room.south
    elif direction == "e":
        nextRoomID = room.east
    elif direction == "w":
        nextRoomID = room.west
    if nextRoomID is not None and nextRoomID > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        player.currentRoom=nextRoomID
        player.save()
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        for p_uuid in currentPlayerUUIDs:
            pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        for p_uuid in nextPlayerUUIDs:
            pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name':player.user.username, 'room_id': nextRoom.id, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)
        return JsonResponse({'name':player.user.username, 'room_id': room.id, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    data = json.loads(request.body)
    player = request.user.player
    room = player.room()
    players_in_room = room.playerUUIDs(player.uuid)
    pusher.trigger(f'p-channel-{player.uuid}', u'broadcast', {'message': f'You say "{data["message"]}"'})
    for p_uuid in players_in_room:
            pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} says "{data["message"]}".'})
    return JsonResponse({'message':"Totally implemented"}, safe=True)


@csrf_exempt
@api_view(["POST"])
def shout(request):
    data = json.loads(request.body)
    player = request.user.player
    room = player.room()
    pusher.trigger(f'main-channel', u'broadcast', {'message':f'{player.user.username} (Room: {room.title}) shouts "{data["message"]}".'})
    return JsonResponse({'message':"Totally implemented"}, safe=True)


@csrf_exempt
@api_view(["POST"])
def whisper(request):
    data = json.loads(request.body)
    player = request.user.player
    target = User.objects.get(username = data.target)
    target_uuid = target.player.uuid
    room = player.room()
    pusher.trigger(f'p-channel-{target_uuid}', u'broadcast', {'message':f'{player.user.username} (Room: {room.title}) whispers "{data["message"]}".'})
    return JsonResponse({'message':"Totally implemented"}, safe=True)
