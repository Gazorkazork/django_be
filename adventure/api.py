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
            'west': i.west,
        } for i in planet_rooms]
    }
    rooms_visited = PlayerVisited.objects.filter(player=player)
    visited_list = [i.room.id for i in rooms_visited]
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name': player.user.username, 'inventory': player.items(), 'room_id': room.id, 'title': room.title, 'description': room.description, 'room_items': room.items(), 'planet_map': planet_map, 'visited': visited_list, 'players': players}, safe=True)


@csrf_exempt
@api_view(["POST"])
def move(request):
    dirs = {"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    items = room.items()
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
        player.currentRoom = nextRoomID
        player.save()
        description = nextRoom.description
        if player.hasVisited(nextRoom) and nextRoom.description_b:
            description = nextRoom.description_b
        if not player.hasVisited(room):
            PlayerVisited.objects.create(player=player, room=room)
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        rooms_visited = PlayerVisited.objects.filter(player=player)
        visited_list = [i.room.id for i in rooms_visited]
        pusher.trigger(f'p-channel-{player.uuid}', u'broadcast', {
            'message': f'You walk {dirs[direction]}.'})
        for p_uuid in currentPlayerUUIDs:
            pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {
                           'message': f'{player.user.username} has walked {dirs[direction]}.'})
        for p_uuid in nextPlayerUUIDs:
            pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {
                           'message': f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name': player.user.username, 'inventory': player.items(), 'room_id': nextRoom.id, 'title': nextRoom.title, 'description': description, 'room_items': nextRoom.items(), 'players': players, 'visited': visited_list, 'error_msg': ""}, safe=True)
    else:
        players = room.playerNames(player_id)
        description = room.description
        if player.hasVisited(room) and room.description_b:
            description = nextRoom.description_b
        pusher.trigger(f'p-channel-{player.uuid}', u'broadcast', {
            'message': 'You cannot go that way.'})
        return JsonResponse({'name': player.user.username, 'inventory': player.items(), 'room_id': room.id, 'title': room.title, 'description': description, 'room_items': room.items(), 'players': players, 'error_msg': "You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def get_item(request):
    player = request.user.player
    player_id = player.id
    data = json.loads(request.body)
    item_id = data['item']
    try:
        item = Item.objects.get(id=item_id)
    except:
        return JsonResponse({'error_msg': "No such item."})
    room = player.room()
    try:
        ri = RoomItem.objects.get(room=room, item=item)
    except:
        return JsonResponse({'error_msg': "No such item in this room."})
    if ri.amount == 1 and not ri.respawn:
        ri.delete()
    elif ri.amount > 0:
        ri.amount -= 1
        ri.last_taken = datetime.datetime.now()
        ri.save()
    else:
        if ri.last_taken + datetime.timedelta(seconds=ri.respawn) < datetime.datetime.now():
            return JsonResponse({'error_msg': "None left. Wait for respawn."})
        else:
            ri.last_taken = datetime.datetime.now()
            ri.save()
    try:
        pi = PlayerItem.objects.get(player=player, item=item)
        pi.amount += 1
    except PlayerItem.DoesNotExist:
        pi = PlayerItem(player=player, item=item)
    pi.save()
    currentPlayerUUIDs = room.playerUUIDs(player_id)
    pusher.trigger(f'p-channel-{player.uuid}', u'broadcast',
                   {'message': f'You picked up {item.name}.'})
    for p_uuid in currentPlayerUUIDs:
        pusher.trigger(f'p-channel-{p_uuid}', u'broadcast',
                       {'message': f'{player.user.username} picked up {item.name}.'})
    return JsonResponse({'inventory': player.items(), 'room_items': room.items()})


@csrf_exempt
@api_view(["POST"])
def drop_item(request):
    player = request.user.player
    player_id = player.id
    data = json.loads(request.body)
    item_id = data['item']
    try:
        item = Item.objects.get(id=item_id)
    except:
        return JsonResponse({'error_msg': "No such item."})
    room = player.room()
    try:
        pi = PlayerItem.objects.get(player=player, item=item)
    except:
        return JsonResponse({'error_msg': "No such item in inventory."})
    if pi.amount > 1:
        pi.amount -= 1
        pi.save()
    else:
        pi.delete()
    try:
        ri = RoomItem.objects.get(room=room, item=item)
        ri.amount += 1
    except RoomItem.DoesNotExist:
        ri = RoomItem(room=room, item=item)
    ri.save()
    currentPlayerUUIDs = room.playerUUIDs(player_id)
    pusher.trigger(f'p-channel-{player.uuid}', u'broadcast',
                   {'message': f'You dropped {item.name}.'})
    for p_uuid in currentPlayerUUIDs:
        pusher.trigger(f'p-channel-{p_uuid}', u'broadcast',
                       {'message': f'{player.user.username} picked up {item.name}.'})
    return JsonResponse({'inventory': player.items(), 'room_items': room.items()})


@csrf_exempt
@api_view(["POST"])
def look_item(request):
    player = request.user.player
    data = json.loads(request.body)
    target_id = data['target']
    try:
        item = Item.objects.get(id=target_id)
    except:
        return JsonResponse({'error_msg': "No such item."})

    if (
        PlayerItem.objects.filter(player=player, item=item).exists() or 
        RoomItem.objects.filter(room=player.room(), item=item).exists()
    ):
        pusher.trigger(f'p-channel-{player.uuid}', u'broadcast', {'message': item.description})
        return JsonResponse({'status': 200})
    else:
        return JsonResponse({'error_msg': "No such item here."})


@csrf_exempt
@api_view(["POST"])
def say(request):
    data = json.loads(request.body)
    player = request.user.player
    room = player.room()
    players_in_room = room.playerUUIDs(player.id)
    pusher.trigger(f'p-channel-{player.uuid}', u'broadcast',
                   {'message': f'You say "{data["message"]}"'})
    for p_uuid in players_in_room:
        pusher.trigger(f'p-channel-{p_uuid}', u'broadcast',
                       {'message': f'{player.user.username} says "{data["message"]}".'})
    return JsonResponse({'message': "Totally implemented"}, safe=True)


@csrf_exempt
@api_view(["POST"])
def shout(request):
    data = json.loads(request.body)
    player = request.user.player
    room = player.room()
    pusher.trigger(f'p-channel-{player.uuid}', u'broadcast', {
                   'message': f'You shout "{data["message"]}".'})
    pusher.trigger(f'main-channel', u'broadcast',
                   {'message': f'{player.user.username} (Room: {room.title}) shouts "{data["message"]}".'})
    return JsonResponse({'message': "Totally implemented"}, safe=True)


@csrf_exempt
@api_view(["POST"])
def whisper(request):
    data = json.loads(request.body)
    player = request.user.player
    target = User.objects.get(username=data["target"])
    target_uuid = target.player.uuid
    room = player.room()
    pusher.trigger(f'p-channel-{player.uuid}', u'broadcast', {
                   'message': f'You whisper to {data["target"]} "{data["message"]}".'})
    pusher.trigger(f'p-channel-{target_uuid}', u'broadcast', {
                   'message': f'{player.user.username} (Room: {room.title}) whispers "{data["message"]}".'})
    return JsonResponse({'message': "Totally implemented"}, safe=True)
