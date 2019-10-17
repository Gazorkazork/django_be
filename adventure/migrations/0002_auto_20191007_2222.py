# Generated by Django 2.2.5 on 2019-09-23 18:04

from django.db import migrations
import random

seed = {
    "0_0": {"coord_x": 0, "coord_y": 0, "north": None, "south": (0, -1), "east": (1, 0), "west": (-1, 0)}, "-1_0": {"coord_x": -1, "coord_y": 0, "north": (-1, 1), "south": (-1, -1), "east": (0, 0), "west": None}, "0_-1": {"coord_x": 0, "coord_y": -1, "north": (0, 0), "south": (0, -2), "east": (1, -1), "west": None}, "1_0": {"coord_x": 1, "coord_y": 0, "north": (1, 1), "south": (1, -1),
    "east": (2, 0), "west": (0, 0)}, "1_1": {"coord_x": 1, "coord_y": 1, "north": (1, 2), "south": (1, 0), "east": (2, 1), "west": None}, "-1_1": {"coord_x": -1, "coord_y": 1, "north": (-1, 2), "south": (-1, 0), "east": None, "west": (-2, 1)}, "2_1": {"coord_x": 2, "coord_y": 1, "north": None, "south": None, "east": (3, 1), "west": (1, 1)}, "3_1": {"coord_x": 3, "coord_y": 1, "north": (3, 2), "south": (3, 0), "east": (4, 1), "west": (2, 1)}, "1_-1": {"coord_x": 1, "coord_y": -1, "north": (1, 0), "south": None, "east": (2, -1), "west": (0, -1)}, "3_2": {"coord_x": 3, "coord_y": 2, "north": None, "south": (3, 1), "east": None, "west": None}, "0_-2": {"coord_x": 0, "coord_y": -2, "north": (0, -1), "south": None, "east": None, "west": (-1, -2)}, "-1_-2": {"coord_x": -1, "coord_y": -2, "north": (-1, -1), "south": (-1, -3), "east": (0, -2), "west": (-2, -2)}, "2_-1": {"coord_x": 2, "coord_y": -1, "north": (2, 0), "south": (2, -2), "east": None, "west": (1, -1)}, "-1_2": {"coord_x": -1, "coord_y": 2, "north": None, "south": (-1, 1), "east": None, "west": (-2, 2)}, "1_2": {"coord_x": 1, "coord_y": 2, "north": (1, 3), "south": (1, 1), "east": None, "west": None}, "4_2": {"coord_x": 4, "coord_y": 2, "north": (4, 3), "south": (4, 1), "east": (5, 2), "west": None}, "5_2": {"coord_x": 5, "coord_y": 2, "north": (5, 3), "south": None, "east": (6, 2), "west": (4, 2)}, "-1_-3": {"coord_x": -1, "coord_y": -3, "north": (-1, -2), "south": None, "east": (0, -3), "west": (-2, -3)}, "3_0": {"coord_x": 3, "coord_y": 0, "north": (3, 1), "south": None, "east": (4, 0), "west": None}, "5_3": {"coord_x": 5, "coord_y": 3, "north": (5, 4), "south": (5, 2), "east": (6, 3), "west": None}, "1_3": {"coord_x": 1, "coord_y": 3, "north": (1, 4), "south": (1, 2), "east": (2, 3), "west": (0, 3)}, "0_-3": {"coord_x": 0, "coord_y": -3, "north": None, "south": (0, -4), "east": (1, -3), "west": (-1, -3)}, "-2_1": {"coord_x": -2, "coord_y": 1, "north": (-2, 2), "south": None, "east": (-1, 1), "west": (-3, 1)}, "-2_2": {"coord_x": -2, "coord_y": 2, "north": None, "south": (-2, 1), "east": (-1, 2), "west": (-3, 2)}, "4_0": {"coord_x": 4, "coord_y": 0, "north": (4, 1), "south": None, "east": (5, 0), "west": (3, 0)}, "2_-2": {"coord_x": 2, "coord_y": -2, "north": (2, -1), "south": None, "east": (3, -2), "west": None}, "3_-2": {"coord_x": 3, "coord_y": -2, "north": None, "south": (3, -3), "east": None, "west": (2, -2)}, "-2_-2": {"coord_x": -2, "coord_y": -2, "north": None, "south": None, "east": (-1, -2), "west": (-3, -2)}, "3_-3": {"coord_x": 3, "coord_y": -3, "north": (3, -2), "south": (3, -4), "east": (4, -3), "west": None}, "4_-3": {"coord_x": 4, "coord_y": -3, "north": None, "south": (4, -4), "east":
    (5, -3), "west": (3, -3)}, "4_1": {"coord_x": 4, "coord_y": 1, "north": (4, 2), "south": (4, 0), "east": None, "west": (3, 1)}, "-3_-2": {"coord_x": -3, "coord_y": -2, "north": (-3, -1), "south": (-3, -3), "east": (-2, -2), "west": None}, "4_3": {"coord_x": 4, "coord_y": 3, "north": None, "south": (4, 2), "east": None, "west": None}, "-3_2": {"coord_x": -3, "coord_y": 2, "north": None, "south": None, "east": (-2, 2), "west": None}, "1_4": {"coord_x": 1, "coord_y": 4, "north": (1, 5), "south": (1, 3), "east": None, "west": (0, 4)}, "-3_-1": {"coord_x": -3, "coord_y": -1, "north": None, "south": (-3, -2), "east": None, "west": (-4, -1)}, "0_3": {"coord_x": 0, "coord_y": 3, "north": (0, 4), "south": None, "east": (1, 3), "west": (-1, 3)}, "-4_-2": {"coord_x": -4, "coord_y": -2, "north": (-4, -1), "south": (-4, -3), "east": None, "west": (-5, -2)}, "2_0": {"coord_x": 2, "coord_y": 0, "north": None, "south": (2, -1), "east": None, "west": (1, 0)}, "-3_-3": {"coord_x": -3, "coord_y": -3, "north": (-3, -2), "south": (-3, -4), "east": (-2, -3), "west": (-4, -3)}, "-2_-3": {"coord_x": -2, "coord_y": -3, "north": None, "south": None, "east": (-1, -3), "west": (-3, -3)}, "3_-4": {"coord_x": 3, "coord_y": -4, "north": (3, -3), "south": (3, -5), "east": None, "west": None}, "5_-3": {"coord_x": 5, "coord_y": -3, "north": (5, -2), "south": None, "east": None, "west": (4, -3)}, "2_3": {"coord_x": 2, "coord_y": 3, "north": None, "south": None, "east": None, "west": (1, 3)}, "0_-4": {"coord_x": 0, "coord_y": -4, "north": (0, -3), "south": (0, -5), "east": (1, -4), "west": (-1, -4)}, "-3_3": {"coord_x": -3, "coord_y": 3, "north": (-3, 4), "south": None, "east": (-2, 3), "west": (-4, 3)}, "-1_-1": {"coord_x": -1, "coord_y": -1, "north": (-1, 0), "south": (-1, -2), "east": None, "west": None}, "5_0": {"coord_x": 5, "coord_y": 0, "north": None, "south": None, "east": None, "west": (4, 0)}, "4_-4": {"coord_x": 4, "coord_y": -4, "north": (4, -3), "south": None, "east": None, "west": None}, "5_4": {"coord_x": 5, "coord_y": 4, "north": None, "south": (5, 3), "east": None, "west": None}, "3_-5": {"coord_x": 3, "coord_y": -5, "north": (3, -4), "south": (3, -6), "east": (4, -5), "west": (2, -5)}, "6_2": {"coord_x": 6, "coord_y": 2, "north": None, "south": (6, 1), "east": None, "west": (5, 2)}, "1_5": {"coord_x": 1, "coord_y": 5, "north": (1, 6), "south": (1, 4), "east": (2, 5), "west": None}, "3_-6": {"coord_x": 3, "coord_y": -6, "north": (3, -5), "south": None, "east": None, "west": None}, "-4_-3": {"coord_x": -4, "coord_y": -3, "north": (-4, -2), "south": None, "east": (-3, -3), "west": None}, "-5_-3": {"coord_x": -5, "coord_y": -3, "north": None, "south": (-5, -4), "east": None,
    "west": (-6, -3)}, "0_-5": {"coord_x": 0, "coord_y": -5, "north": (0, -4), "south": None, "east": (1, -5), "west": (-1, -5)}, "-1_3": {"coord_x": -1, "coord_y": 3, "north": (-1, 4), "south": None, "east": (0, 3), "west": (-2, 3)}, "-1_-4": {"coord_x": -1, "coord_y": -4, "north": None, "south": None, "east": (0, -4), "west": None}, "2_5": {"coord_x": 2, "coord_y": 5, "north": None, "south": (2, 4), "east": (3, 5), "west": (1, 5)}, "0_4": {"coord_x": 0, "coord_y": 4, "north": None, "south": (0, 3), "east": (1, 4), "west": (-1, 4)}, "2_4": {"coord_x": 2, "coord_y": 4, "north": (2, 5), "south": None, "east": (3, 4), "west": None}, "1_-5": {"coord_x": 1, "coord_y": -5, "north": (1, -4), "south": None, "east": (2, -5), "west": (0, -5)}, "2_-5": {"coord_x": 2, "coord_y": -5, "north": None, "south": None, "east": (3, -5), "west": (1, -5)}, "5_-2": {"coord_x": 5, "coord_y": -2, "north": (5, -1), "south": (5, -3), "east": (6, -2), "west": None}, "1_-3": {"coord_x": 1, "coord_y": -3, "north": None, "south": None, "east": None, "west": (0, -3)}, "-4_-4": {"coord_x": -4, "coord_y": -4, "north": None, "south": (-4, -5), "east": None, "west": (-5, -4)}, "3_4": {"coord_x": 3, "coord_y": 4, "north": (3, 5), "south": None, "east": None, "west": (2, 4)}, "1_-4": {"coord_x": 1, "coord_y": -4, "north": None, "south": (1, -5), "east": None, "west": (0, -4)}, "5_-1": {"coord_x": 5, "coord_y": -1, "north": None, "south": (5, -2), "east": None, "west": None}, "-5_-4": {"coord_x": -5, "coord_y": -4, "north": (-5, -3), "south": None, "east": (-4, -4), "west": None}, "3_5": {"coord_x": 3, "coord_y": 5, "north": None, "south": (3, 4), "east": (4, 5), "west": (2, 5)}, "4_-5": {"coord_x": 4, "coord_y": -5, "north": None, "south": None, "east": None, "west": (3, -5)}, "-5_-2": {"coord_x": -5, "coord_y": -2, "north": (-5, -1), "south": None, "east": (-4, -2), "west": None}, "6_-2": {"coord_x": 6, "coord_y": -2, "north": None, "south": None, "east": None, "west": (5, -2)}, "-6_-3": {"coord_x": -6, "coord_y": -3, "north": (-6, -2), "south": None, "east": (-5, -3), "west": None}, "6_3": {"coord_x": 6, "coord_y": 3, "north": None, "south": None, "east": None, "west": (5, 3)}, "-3_4": {"coord_x": -3, "coord_y": 4, "north": (-3, 5), "south": (-3, 3), "east": None, "west": None}, "1_6": {"coord_x": 1, "coord_y": 6, "north": (1, 7), "south": (1, 5), "east": (2, 6), "west": None}, "-1_4": {"coord_x": -1, "coord_y": 4, "north": (-1, 5), "south": (-1, 3), "east": (0, 4), "west": None}, "2_6": {"coord_x": 2,
    "coord_y": 6, "north": None, "south": None, "east": (3, 6), "west": (1, 6)}, "-6_-2": {"coord_x": -6, "coord_y": -2, "north": None, "south": (-6, -3), "east": None, "west": None}, "6_1": {"coord_x": 6, "coord_y": 1, "north": (6, 2), "south": None, "east": None, "west": None}, "3_6": {"coord_x": 3, "coord_y": 6, "north": None, "south": None, "east": None, "west": (2, 6)}, "-1_-5": {"coord_x": -1, "coord_y": -5, "north": None, "south": None, "east": (0, -5), "west": None}, "-5_-1": {"coord_x": -5, "coord_y": -1, "north": (-5, 0), "south": (-5, -2), "east": (-4, -1), "west": (-6, -1)}, "4_5": {"coord_x": 4, "coord_y": 5, "north": None, "south": None, "east": None, "west": (3, 5)}, "-4_3": {"coord_x": -4, "coord_y": 3, "north": None, "south": None, "east": (-3, 3), "west": (-5, 3)}, "-4_-1": {"coord_x": -4, "coord_y": -1, "north": None, "south": (-4, -2), "east": (-3, -1), "west": (-5, -1)}, "-4_-5": {"coord_x": -4, "coord_y": -5, "north": (-4, -4), "south": None, "east": (-3, -5), "west": None}, "-3_-4": {"coord_x": -3, "coord_y": -4, "north": (-3, -3), "south": (-3, -5), "east": None, "west": None}, "-2_4": {"coord_x": -2, "coord_y": 4, "north": None, "south": (-2, 3), "east": None, "west": None}, "-3_1": {"coord_x": -3, "coord_y": 1, "north": None, "south": None, "east": (-2, 1), "west": None}, "-2_3": {"coord_x": -2, "coord_y": 3, "north": (-2, 4), "south": None, "east": (-1, 3), "west": (-3, 3)}, "-3_-5": {"coord_x": -3, "coord_y": -5, "north": (-3, -4), "south": None, "east": None, "west": (-4, -5)}, "-5_3": {"coord_x": -5, "coord_y": 3, "north": None, "south": None, "east": (-4, 3), "west": None}, "-6_-1": {"coord_x": -6, "coord_y": -1, "north": None, "south": None, "east": (-5, -1), "west": None}, "1_7": {"coord_x": 1, "coord_y": 7, "north": None, "south": (1, 6), "east": None, "west": None}, "-1_5": {"coord_x": -1, "coord_y": 5, "north": None, "south": (-1, 4), "east": None, "west": None}, "-5_0": {"coord_x": -5, "coord_y": 0, "north": None, "south": (-5, -1), "east": None, "west": None}, "-3_5": {"coord_x": -3, "coord_y": 5, "north": None, "south": (-3, 4), "east": None, "west": None}
}

planet = 0

root_name = "Landing Site"
root_description = "After a long journey through space, you finally arrive at the planet Gazorkazork.  You land your ship in the middle of what appears to be an abandoned city.   Your sensors show that it's safe to walk around without extra life support.  Adventure awaits!"
root_description_b = "You feel as though you've been here before.  It's a strange new planet light years from home though so that's impossible.  And yet...  Wait.  No.  There's your ship.  You have been here before.  It seems you've doubled back on your path."

room_attr_a = [
    {"name": "Ugly", "desc":"it looks absolutely hideous."},
    {"name": "Ornate", "desc":"it seems to be very intricately built."},
    {"name": "Crude", "desc":"it looks pretty slapdash.  Like it was put together in minutes, poorly."},
    {"name": "Fantastic", "desc":"it is absolutely awe-inspiring."},
    {"name": "Abandoned", "desc":"it looks like no one has been here in quite some time."},
    {"name": "Decrepit", "desc":"it looks like the whole thing could collapse at any minute."},
    {"name": "Sleek", "desc":"it seems to be very efficiently built. Functional, yet attractive."},
    {"name": "Chilly", "desc":"it looks like the elements have begun to break through. It is chilly here."},
    {"name": "Shiny", "desc":"there are a great many twinkling objects here."},
    {"name": "Plain", "desc":"it is very boring."},
    {"name": "Picturesque", "desc": "it is very beautiful."},
    {"name": "Drafty", "desc":"there appears to be some structural damage. It is... windy."},
    {"name": "Rusting", "desc":"it looks old and decayed."},
    {"name": "Peaceful", "desc":"it is serene and quiet."},
]
room_attr_b = [
    {"name": "Dark", "desc": "It is too dark to see too much, but from what you can see "},
    {"name": "Bright", "desc": "There is a lot of light in here, so much that your eyes are hurting.  Beyond the light, you notice that "},
    {"name": "Glowing", "desc": "Parts of this place seem to be glowing.  You hope it's safe.  Also, you note that "},
    {"name": "Round", "desc": "The room is vaguely round shaped, and "},
    {"name": "Oblong", "desc": "The place reminds you a bit of an egg, not quite a perfect circle.  Oblong, you could say.  Also, "},
    {"name": "Spherical", "desc": "You notice two things about it: First, it is almost perfectly spherical.  Second, "},
    {"name": "Cylindrical", "desc": "The walls curve about, making the whole place seem like a big tube.  You note that "},
    {"name": "Spiraling", "desc": "The geometry here is a bit dizzying, curving around the center.  After taking a second to steady yourself, you form an opinion: "},
    {"name": "Twisted", "desc": "The room seems... battle-scarred?  Like something has damaged the walls.  Also, "},
    {"name": "Labyrinthine", "desc": "The place seems to somehow twist in on itself, forming almost into a maze.  You decide "},
    {"name": "Tortuous", "desc": "The path through is winding and loops back to an almost ridiculous degree.  It is tortuous.  (Tortuous means winding and twisted, by the way. You make a mental note to thank your word-of-the-day calendar.) After reorienting yourself, you decide "},
    {"name": "Pentagonal", "desc": "There are five walls here. Which is peculiar, since all the rooms around here so far seem to be arranged in a near-perfect rectangular grid. Where does the fifth wall go, you wonder? Curious. Anyway, "},
    {"name": "Spacious", "desc": "This room is HUGE!  It echos your steps as you walk.  Yet, "},
    {"name": "Cramped", "desc": "The ceiling is low and you must crawl to move.  Nevertheless, "},
    {"name": "Cavernous", "desc": "You yell, 'ECHOOO!!!' inside to test the acoustics.  Amused, you notice "},
    {"name": "Miniscule", "desc": "You marvel at how small the room is.  The people who made this must have been a fraction of your height.  You notice that "},
    {"name": "Chrome", "desc": "Everything in here appears to be crafted from a dark, mysterious metal. You don't know what the metal is, but you do know "},
    {"name": "Granite", "desc": "You notice that this room has been carved out from a single stone. It has very smooth walls and no corners. You see that "},
    {"name": "Crystal", "desc": "You stand in awe at the sight of light dancing of the many facets in this area.  You conclude that "},
]
room_attr_c = [
    {"name": "Corridor", "desc": "You stand in a corridor.  "},
    {"name": "Hallway", "desc": "You find yourself in a hallway.  "},
    {"name": "Passage", "desc": "You're at the end of a passage.  "},
    {"name": "Storeroom", "desc": "You look around a storeroom.  "},
    {"name": "Observatory", "desc": "After a bit of climbing, you stand in an observatory.  "},
    {"name": "Chamber", "desc": "You've discovered a mostly empty room.  "},
    {"name": "Amphitheater", "desc": "Before you is a room you can only describe as an amphitheater.  "},
    {"name": "Power Room", "desc": "You have emerged into a humming power room.  "},
    {"name": "Control Room", "desc": "You stand in the middle of a room surrounded by blinking screens and buttons.  "},
    {"name": "Comm Center", "desc": "You play with a couple of the headsets in a comm center.  Turning dials and knobs to see if you can reach anoyone.  "},
    {"name": "Workshop", "desc": "With this many tools everywhere, this must be a workshop.  "}, 
    {"name": "Rotunda", "desc": "You decide to call this room a rotunda. Not necessarily because of its shape, because it looks vaguely Greek to you.  "}, 
    {"name": "Garden", "desc": "You are in an indoor garden. You find a bench and decide to sit and rest.  "},
    {"name": "Kitchen", "desc": "Pots, pans, and utensils scatter the room. You look around the kitchen for something edible.  "},
    {"name": "Temple", "desc": "You see strange idols from what you assume are different religions.  This must be a temple.  "},
    {"name": "Infirmary", "desc": "Surrounded by medical tools, you assure yourself that you're in an infirmary.  "},
    {"name": "Atrium", "desc": "This room seems to be an entryway of sorts, though to what you couldn't guess.  "},
    {"name": "Foyer", "desc": "You stand in... you suppose it looks like a waiting room. Of sorts.  "},
]

total_options = len(room_attr_c) * len(room_attr_b) * len(room_attr_a)
remaining = [i for i in range(len(room_attr_c) * len(room_attr_b) * len(room_attr_a))]
room_info = []

while len(room_info) < 101:
    new_num = (random.choice(remaining))
    remaining.remove(new_num)

    divisor = total_options / len(room_attr_a)
    a_multiple = int(new_num / divisor)
    remainder1 = int(new_num % divisor)
    a = room_attr_a[a_multiple]

    divisor = divisor / len(room_attr_b)
    b_multiple = int(remainder1 / divisor)
    remainder2 = int(remainder1 % divisor)
    b = room_attr_b[b_multiple]

    c = room_attr_c[remainder2]

    room_info.append({
        "name": f"{a['name']} {b['name']} {c['name']}",
        "description": f"{c['desc']}{b['desc']}{a['desc']}"
    })

def make_rooms(apps, schema_editor):
    level = seed
    Room = apps.get_model("adventure", "Room")
    db_alias = schema_editor.connection.alias
    rooms = []
    for key in level:
        coord = key.split("_")
        current_info = room_info.pop()
        if key is not "0_0":
            rooms.append(
                Room(
                    planet = planet,
                    coord_x = coord[0],
                    coord_y = coord[1],
                    title = current_info["name"],
                    description = current_info["description"]
                ),
            )
        else:
            rooms.append(
                Room(
                    planet = planet,
                    coord_x = coord[0],
                    coord_y = coord[1],
                    title = root_name,
                    description = root_description,
                    description_b = root_description_b
                ),
            )

    Room.objects.using(db_alias).bulk_create(rooms)

def delete_rooms(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Room = apps.get_model("adventure", "Room")
    Room.objects.using(db_alias).delete()

def connect_rooms(apps, schema_editor):
    level = seed
    db_alias = schema_editor.connection.alias
    Room = apps.get_model("adventure", "Room")
    for key in level:
        coord = key.split("_")
        seed_room = level[key]
        db_room = Room.objects.using(db_alias).filter(
            planet = planet,
            coord_x = coord[0],
            coord_y = coord[1]
        )[0]
        for direc in ["north", "south", "east", "west"]:
            if seed_room[direc]:
                dest = Room.objects.using(db_alias).filter(
                    planet = planet,
                    coord_x = seed_room[direc][0],
                    coord_y = seed_room[direc][1]
                )[0]
                setattr(db_room, direc, dest.id)
        db_room.save()

class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]


    operations = [
        migrations.RunPython(make_rooms, delete_rooms),
        migrations.RunPython(connect_rooms, delete_rooms)
    ]
