import random

room_attr_a = ["Ugly", "Ornate", "Crude", "Dark", "Brilliant", "Fetid", "Sleek", "Chilly", "Shiny", "Plain"]
room_attr_b = ["White", "Black", "Red", "Blue", "Yellow", "Green", "Orange", "Purple", "Brown", "Pink"]
room_attr_c = ["Kitchen", "Garden", "Passage", "Storeroom", "Jail", "Crypt", "Observatory", "Armory", "Barracks", "Chamber"]

remaining = [i for i in range(1000)]
rooms = []

while len(rooms) < 100:
    new_num = (random.choice(remaining))
    remaining.remove(new_num)
    new_num = str(new_num)
    if len(new_num) == 1:
        new_num = "00" + new_num
    if len(new_num) == 2:
        new_num = "0" + new_num
    rooms.append(f"{room_attr_a[int(new_num[0])]} {room_attr_b[int(new_num[1])]} {room_attr_c[int(new_num[2])]}")


# Now... how do we connect the rooms? I'd like to do something better than that Pac-Man thing did. Let's spell out the problem.
# 
# We want to control the following things:
# - (rough) center of level
# - total rooms in level
# - max width / length (?)
# - place similar rooms near each other (?)
# 
# Try generating rooms, THEN connections. That way, you get fewer fingers.
# If you do that, you need a way to ensure all rooms are connected. Ugh.
# 
# n rooms, n connections = average of 2 connections per room
# 
# 
# 
# .
"""
01 02 03 04 05 06
07 08 09 10 11 12
13 14 15 16 17 18
19 20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36

so, for a rect with width of x:
left = -1
right = +1
up = -x
down = +x

OR: just do coordinates. Yeah.

(-3, -3) (-2, -3) (-1, -3) ( 0, -3) ( 1, -3) ( 2, -3) ( 3, -3)
(-3, -2) (-2, -2) (-1, -2) ( 0, -2) ( 1, -2) ( 2, -2) ( 3, -2)
(-3, -1) (-2, -1) (-1, -1) ( 0, -1) ( 1, -1) ( 2, -1) ( 3, -1)
(-3,  0) (-2,  0) (-1,  0) ( 0,  0) ( 1,  0) ( 2,  0) ( 3,  0)
(-3,  1) (-2,  1) (-1,  1) ( 0,  1) ( 1,  1) ( 2,  1) ( 3,  1)
(-3,  2) (-2,  2) (-1,  2) ( 0,  2) ( 1,  2) ( 2,  2) ( 3,  2)
(-3,  3) (-2,  3) (-1,  3) ( 0,  3) ( 1,  3) ( 2,  3) ( 3,  3)
"""