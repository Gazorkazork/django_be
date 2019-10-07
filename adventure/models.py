import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Room(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(max_length=500, default="DEFAULT DESCRIPTION")
    description_b = models.CharField(max_length=500, default="")
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
        return [
            p.user.username for p in Player.objects.filter(currentRoom=self.id)
            if p.id != int(currentPlayerID)
        ]
    def playerUUIDs(self, currentPlayerID):
        return [
            p.uuid for p in Player.objects.filter(currentRoom=self.id)
            if p.id != int(currentPlayerID)
        ]


class Planet(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(max_length=500, default="DEFAULT DESCRIPTION")


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
    def hasVisited(self, room):
        try:
            return PlayerVisited.objects.get(player=self, room=room)
        except PlayerVisited.DoesNotExist:
            return False


class PlayerVisited(models.Model):
    player = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        'Room',
        on_delete=models.CASCADE
    )


class MobTemplate(models.Model):
    name = models.CharField(max_length=50, default="DEFAULT NAME")
    description = models.CharField(max_length=500, default="DEFAULT DESCRIPTION")
    max_health = models.IntegerField(default=50)
    exp = models.IntegerField(default=50)
    damage = models.IntegerField(default=50)
    accuracy = models.IntegerField(default=50)
    evasion = models.IntegerField(default=50)
    idle_text = models.CharField(max_length=1000, default="DEFAULT TEXT")
    attack_text = models.CharField(max_length=1000, default="DEFAULT TEXT")


class Mob(models.Model):
    template = models.ForeignKey(
        'MobTemplate',
        on_delete=models.CASCADE
    )
    health = models.IntegerField(default=50)
    location = models.ForeignKey(
        'MobTemplate',
        on_delete=models.SET_NULL
    )
    prev_loc = models.ForeignKey(
        'MobTemplate',
        on_delete=models.SET_NULL
    )
    target = models.CharField(max_length=50, null=True)


@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()
