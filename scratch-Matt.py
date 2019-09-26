import random

room_attr_a = [
    {"name": "Ugly", "desc":"it looks absolutely hideous."},
    {"name": "Ornate", "desc":"it seems to very intricately built."},
    {"name": "Crude", "desc":"it looks pretty slapdash.  Like it was put together in minutes, poorly."},
    {"name": "Fantastic", "desc":"it is absolutely awe-inspiring."},
    {"name": "Abandoned", "desc":"it looks like no one has been here in quite some time."},
    {"name": "Decrepit", "desc":"it looks like the whole thing could collapse any minute."},
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
    {"name": "Miniscule", "desc": "You marvel at how small the room is.  The people who made this must have been a fraction of your height.  You notice "},
    {"name": "Chrome", "desc": "Everything in here appears to be crafted from a dark, mysterious metal. You don't know what the metal is, but you do know "},
    {"name": "Granite", "desc": "You notice that this room has been carved out from a single stone. It has very smooth walls and no corners. You see that "},
    {"name": "Crystal", "desc": "You stand in awe at the sight of light dancing of the many facets in this area.  You conclude "},
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
    {"name": "Atrium", "desc": "This room seems to be an entryway of sorts, though to what you couldn't guess."},
    {"name": "Foyer", "desc": "You stand in... you suppose it looks like a waiting room. Of sorts."},
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

for i in room_info:
    print(i['name'])
    print(i['description'])
    print()
