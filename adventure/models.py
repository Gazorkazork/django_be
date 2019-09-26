from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid


class Room(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(
        max_length=500, default="DEFAULT DESCRIPTION")
    planet = models.IntegerField(default=0)
    coord_x = models.IntegerField(default=0)
    coord_y = models.IntegerField(default=0)
    north = models.IntegerField(default=0)
    south = models.IntegerField(default=0)
    east = models.IntegerField(default=0)
    west = models.IntegerField(default=0)

    def connectRooms(self, destinationRoom, direction):
        destinationRoomID = destinationRoom.id
        try:
            destinationRoom = Room.objects.get(id=destinationRoomID)
        except Room.DoesNotExist:
            print("That room does not exist")
        else:
            if direction == "north":
                self.north = destinationRoomID
            elif direction == "south":
                self.south = destinationRoomID
            elif direction == "east":
                self.east = destinationRoomID
            elif direction == "west":
                self.west = destinationRoomID
            else:
                print("Invalid direction")
                return
            self.save()

    def playerNames(self, currentPlayerID):
        return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]

    def playerUUIDs(self, currentPlayerID):
        return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]

    def items(self):
        output = []
        room_items = [ri for ri in RoomItem.objects.filter(room=self)]
        for room_item in room_items:
            output.append({
                "item": Item.objects.get(id=room_item.item),
                "amount": room_item.amount,
                "last_taken": models.DateTimeField(default=None),
                "respawn": models.DurationField()
            })
        return output

    def interactables(self):
        output = []
        room_ints = [
            ri for ri in RoomInteractable.objects.filter(room=self.id)]
        for room_int in room_ints:
            output.append({
                "interactable": Interactable.objects.get(id=room_int.interactable),
                "status": room_int.status
            })
        return output


class Planet(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(
        max_length=500, default="DEFAULT DESCRIPTION")


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currentRoom = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def initialize(self):
        if self.currentRoom == 0:
            self.currentRoom = Room.objects.first().id
            self.save()

    def room(self):
        try:
            return Room.objects.get(id=self.currentRoom)
        except Room.DoesNotExist:
            self.initialize()
            return self.room()

    def items(self):
        output = []
        player_items = [pi for pi in PlayerItem.objects.filter(player=self)]
        for player_item in player_items:
            output.append({
                "item": Item.objects.get(id=player_item.item),
                "amount": player_item.amount
            })
        return output


class Interactable(models.Model):
    name = models.CharField(max_length=50, default="DEFAULT INTERACTABLE")
    description = models.CharField(
        max_length=500, default="DEFAULT DESCRIPTION")


class Item(models.Model):
    name = models.CharField(max_length=50, default="DEFAULT ITEM")
    description = models.CharField(
        max_length=500, default="DEFAULT DESCRIPTION")
    item_type = models.CharField(max_length=50, default="DEFAULT TYPE")


class PlayerItem(models.Model):
    player = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE
    )
    amount = models.IntegerField(default=1)


class RoomInteractable(models.Model):
    room = models.ForeignKey(
        'Room',
        on_delete=models.CASCADE
    )
    interactable = models.ForeignKey(
        'Interactable',
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=50, default="DEFAULT STATUS")


class RoomItem(models.Model):
    room = models.ForeignKey(
        'Room',
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE
    )
    amount = models.IntegerField(default=1)
    last_taken = models.DateTimeField(default=None)
    respawn = models.DurationField(default=None)


@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()
