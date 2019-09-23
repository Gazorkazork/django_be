import random

room_attr_a = ["Ugly", "Ornate", "Crude", "Dark",
               "Brilliant", "Fetid", "Sleek", "Chilly", "Shiny", "Plain"]
room_attr_b = ["White", "Black", "Red", "Blue", "Yellow",
               "Green", "Orange", "Purple", "Brown", "Pink"]
room_attr_c = ["Kitchen", "Garden", "Passage", "Storeroom",
               "Jail", "Crypt", "Observatory", "Armory", "Barracks", "Chamber"]

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
    rooms.append(
        f"{room_attr_a[int(new_num[0])]} {room_attr_b[int(new_num[1])]} {room_attr_c[int(new_num[2])]}")
