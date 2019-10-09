
import random
from django.db import migrations
from datetime import timedelta

item_seed = [
    {
        "name": "Laser Boots",
        "desc": "It's a pair of laser boots! There seems to be a bit of wear and tear, and one of the lasers looks like it may need a new diode, but hey, free boots."
    },
    {
        "name": "Rusty Crowbar",
        "desc": "An old crowbar. Quite hefty. Quite rusty. Probably good for hitting things."
    },
    {
        "name": "Strange Goo",
        "desc": "It's... gooey."
    },
    {
        "name": "OLA Free Trial CD",
        "desc": "It's been a while since you've seen one of these! A genuine OAL free trial compact disk. You remember an urban legend that some of these were blasted into space to cut down the clutter on Earth. It looks like it wasn't just a myth! You wonder if you could still get 30 minutes of internet out of it..."
    },
]


def make_items(apps, schema_editor):
    Item = apps.get_model("adventure", "Item")
    item_group = []
    db_alias = schema_editor.connection.alias
    for key in item_seed:
        item_group.append(
            Item(
                name=key["name"],
                description=key["desc"]
            ),
        )

    Item.objects.using(db_alias).bulk_create(item_group)


def delete_items(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Item = apps.get_model("adventure", "Item")
    Item.objects.using(db_alias).delete()


def place_items(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Item = apps.get_model("adventure", "Item")
    Room = apps.get_model("adventure", "Room")
    RoomItem = apps.get_model("adventure", "RoomItem")

    room_items = []

    rooms = Room.objects.all()
    items = Item.objects.all()

    for r in rooms:
        for i in items:
            if random.random() < .2:
                ri = RoomItem(room=r, item=i, respawn=timedelta(seconds=30))
                room_items.append(ri)

    RoomItem.objects.using(db_alias).bulk_create(room_items)


def unplace_items(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Item = apps.get_model("adventure", "Item")
    Item.objects.using(db_alias).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0002_auto_20191007_2222'),
    ]

    operations = [
        migrations.RunPython(make_items, delete_items),
        migrations.RunPython(place_items, unplace_items)
    ]
