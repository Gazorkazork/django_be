import random

class Protoroom:
    # When integrating this into the actual code, replace this
    # class with the actual room class. Adjust as needed.
    def __init__(self, coord, north=None, south=None, east=None, west=None):
        self.coord = coord
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def __repr__(self):
        return f"Protoroom{self.coord}"


def populate_level(rooms, connections, empty_pct, empty_var, spread):
    # Protorooms are arranged around the root at (0, 0). A "ring"
    #   at int "n" is comprised of the spaces "n" distance 
    #   from (0, 0).

    # rooms = number of rooms

    # connections = number of connections between rooms.
    #   (If connections = rooms, there will be an average of
    #   two connections per room.)

    # empty_pct = % of empty spaces per ring around root.
    #   (Enter as pct, i.e. "20" == 20%)

    # empty_var = A random number between 0 and empty_var is
    #   applied to empty_pct for each ring.

    # spread = A ring is considered "filled" when every space
    #   in it is occupied, excluding predetermined empty ones.
    #   Spread indicates how far from the first unfilled
    #   ring a room can be placed.

    # Note: the level may autogenerate with more connections
    #   than requested. Priority is given to ensuring all
    #   rooms are connected.

##### PART 1: BUILD ROOMS #####

    ### HELPER FUNCTIONS ###
    def get_all_from_ring(ring_num):
    # Returns all coordinates at a given distance from the center.
        ring_list = []
        for i in range(ring_num):
            ring_list.extend([(i, ring_num - i), (i, -(ring_num - i)), (ring_num - i, -i), (-(ring_num - i), -i)])
        return ring_list

    def get_empties_from_ring(ring_num, empty_pct, empty_var):
    # Returns a random list of empty spaces at a given distance from the center.
        total_spaces = ring_num * 4
        ring_list = get_all_from_ring(ring_num)
        empty_spaces = round(total_spaces * (.01 * empty_pct) + .01 * (random.random() * empty_var - .5 * empty_var))
        return random.sample(ring_list, empty_spaces)
    
    # initialize
    root = Protoroom((0, 0))
    layout = {root.coord: root}
    empty_coords = []
    closest_available = 1
    remaining = rooms

    # get empty spaces in current rings, add to used_coords
    for ring_num in range(1, spread + 1):
        empty_coords.extend(get_empties_from_ring(ring_num, empty_pct, empty_var))

    # loop for each added room
    while remaining > 0:
        options = []
        checked = False
        while not checked:
            # Check each loop to see if a new ring has opened up
            #   (If it has, get the empties for it)
            checked = True
            to_check = get_all_from_ring(closest_available)
            if all(i in layout or i in empty_coords for i in to_check):
                checked = False
                closest_available += 1
                empty_coords.extend(get_empties_from_ring(closest_available, empty_pct, empty_var))

        for coord in layout:
        # Get list of possible spaces for expansion by checking every space
        #   bordering current layout. If it's available and in an open ring,
        #   add it to the list.
            x = coord[0]
            y = coord[1]
            for neighbor in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                if all(neighbor not in i for i in [layout, empty_coords, options]):
                    if abs(neighbor[0]) + abs(neighbor[1]) <= closest_available + spread:
                        # print(f"{neighbor}:", "DIST:", abs(neighbor[0]) + abs(neighbor[1]), "SPREAD:", closest_available + spread)
                        options.append(neighbor)
        
        # Choose one from possible spaces, create new room with coords 
        #   and place it into layout.
        new_coord = random.choice(options)
        new_room = Protoroom(new_coord)
        layout[new_coord] = new_room
        remaining -= 1
    
##### PART 2: CONNECT ROOMS #####
    
    ### HELPER FUNCTIONS ###
    def check_root_path(start):
    # This iteratively loops through paths from a given point until it finds
    # a way to the root of the level. (If there is no way to the root, it
    # returns the closest point on its path to the center.)
        current = start
        path = [start]
        visited = [start]
        closest = (start, abs(start.coord[0]) + abs(start.coord[1]))
        while True:
            # return "success" if we've reached (0, 0)
            if current.coord == (0, 0):
                return "success"
            else:
                # Check to see if this is the closest point to the center
                if abs(current.coord[0]) + abs(current.coord[0]) < closest[1]:
                    closest = (current, abs(current.coord[0]) + abs(current.coord[0]))
                # Check for ways forward, take first path that hasn't been travelled yet.
                for room in [current.north, current.south, current.east, current.west, "dead_end"]:
                    # If there are no new ways out, go backwards along the
                    # path travelled. If you end up back at the beginning
                    # and are still trapped, there is no way to the center.
                    if room == "dead_end":
                        if len(path) == 1:
                            return closest[0]
                        path.pop()
                        current = path[-1]
                    # When moving to the next room, add it to both the path
                    # and the visited list.
                    elif room and room not in visited:
                        path.append(room)
                        visited.append(room)
                        current = room
                        break

    def all_possible_connections(layout):
    # This grabs all connections between rooms, and sorts
    # them based on active status.
        output = {
            "ns_active": [],
            "ew_active": [],
            "ns_inactive": [],
            "ew_inactive": []
        }
        for coord in layout:
            x = coord[0]
            y = coord[1]
            if (x, y - 1) in layout:
                if layout[coord].south:
                    output["ns_active"].append([coord, (x, y - 1)])
                else:
                    output["ns_inactive"].append([coord, (x, y - 1)])
            if (x - 1, y) in layout:
                if layout[coord].west:
                    output["ew_active"].append([coord, (x - 1, y)])
                else:
                    output["ew_inactive"].append([coord, (x - 1, y)])
        return output
    
    # We now have a contiguous group of rooms based on a single point
    #   that is (likely) in the center of the group, with adjustable 
    #   compactness. It's time to connect the rooms together.

    # First, iterate through all points on the map and make sure each of
    #   them is connected to something (randomly selected from possibilities).
    for coord in layout:
        if not any([layout[coord].north, layout[coord].south, layout[coord].east, layout[coord].west]):
            occupied = []
            x = coord[0]
            y = coord[1]
            for neighbor in [
                {"loc": (x, y + 1), "dir": "north"},
                {"loc": (x, y - 1), "dir": "south"},
                {"loc": (x + 1, y), "dir": "east"},
                {"loc": (x - 1, y), "dir": "west"}
            ]:
                if neighbor["loc"] in layout:
                    occupied.append({"room": layout[neighbor["loc"]], "dir": neighbor["dir"]})
            selected = random.choice(occupied)
            direction = selected["dir"]
            if direction == "north": reverse_dir = "south"
            elif direction == "south": reverse_dir = "north"
            elif direction == "east": reverse_dir = "west"
            elif direction == "west": reverse_dir = "east"
            setattr(layout[coord], direction, selected["room"])
            setattr(selected["room"], reverse_dir, layout[coord])
    
    # Next, make sure all rooms are connected to each other. To do
    #   that, we check to see if they are all connected to the root.
    for coord in layout:
        result = check_root_path(layout[coord])
        while result != "success":
            options = []
            x = result.coord[0]
            y = result.coord[1]
            if not result.west and (x - 1, y) in layout:
                options.append({"room": layout[(x - 1, y)], "dir": "west"})

            if not result.east and (x + 1, y) in layout:
                options.append({"room": layout[(x + 1, y)], "dir": "east"})

            if not result.south and (x, y - 1) in layout:
                options.append({"room": layout[(x, y - 1)], "dir": "south"})

            if not result.north and (x, y + 1) in layout:
                options.append({"room": layout[(x, y + 1)], "dir": "north"})

            if len(options) > 0:
                selected = random.choice(options)
                direction = selected["dir"]
                if direction == "north": reverse_dir = "south"
                elif direction == "south": reverse_dir = "north"
                elif direction == "east": reverse_dir = "west"
                elif direction == "west": reverse_dir = "east"
                setattr(result, direction, selected["room"])
                setattr(selected["room"], reverse_dir, result)
                result = check_root_path(result)
            else:
                if result.north:
                    options.append(result.north)
                if result.south:
                    options.append(result.south)
                if result.east:
                    options.append(result.east)
                if result.west:
                    options.append(result.west)
                result = random.choice(options)
    
    # Get a record of all connections, sorted by active status
    connect = all_possible_connections(layout)

    # Increase number of connections to meet requested amount (if possible)
    while len(connect["ew_active"]) + len(connect["ns_active"]) < connections:
        if len(connect["ew_inactive"]) + len(connect["ns_inactive"]) == 0:
            break
        else:
            if len(connect["ew_inactive"]) == 0 or (random.randint(0, 1) == 0 and len(connect["ns_inactive"]) != 0):                
                new_connect = random.choice(connect["ns_inactive"])
                layout[new_connect[0]].south = layout[new_connect[1]]
                layout[new_connect[1]].north = layout[new_connect[0]]
                connect["ns_inactive"].remove(new_connect)
                connect["ns_active"].append(new_connect)
            else:
                new_connect = random.choice(connect["ew_inactive"])
                layout[new_connect[0]].west = layout[new_connect[1]]
                layout[new_connect[1]].east = layout[new_connect[0]]
                connect["ew_inactive"].remove(new_connect)
                connect["ew_active"].append(new_connect)

    # Done!
    return layout


def convert_to_seed(layout):
    seed = {}
    for coord in layout:
        seed[f"{coord[0]}_{coord[1]}"] = {
            "coord_x": coord[0],
            "coord_y": coord[1],
            "north": layout[coord].north.coord if layout[coord].north else None,
            "south": layout[coord].south.coord if layout[coord].south else None,
            "east": layout[coord].east.coord if layout[coord].east else None,
            "west": layout[coord].west.coord if layout[coord].west else None
        }
    return seed


# TESTING FUNCTIONS
def check_connections(layout):
    for coord in layout:
        room = layout[coord] 
        if room.north:
            if not hasattr(room.north, "south") or room.north.south != room:
                print(f"error: check room.north at coord {coord}")
                return
        if room.south:
            if not hasattr(room.south, "north") or room.south.north != room:
                print(f"error: check room.south at coord {coord}")
                return
        if room.east:
            if not hasattr(room.east, "west") or room.east.west != room:
                print(f"error: check room.east at coord {coord}")
                return
        if room.west:
            if not hasattr(room.west, "east") or room.west.east != room:
                print(f"error: check room.west at coord {coord}")
                return
    print("connections all good.")
    return

def printout(layout, n):
    for col in reversed(range(n)):
        mid = n // 2
        line1 = ""
        line2 = ""
        for row in range(n):
            if (row - mid, col - mid) in layout:
                e = False
                s = False
                if layout[(row - mid, col - mid)].east:
                    e = True
                if layout[(row - mid, col - mid)].south:
                    s = True
                if row - mid < 0:
                    a = f"{row - mid}"
                else:
                    a = f" {row - mid}"
                if col - mid < 0:
                    b = f"{col - mid}"
                else:
                    b = f" {col - mid}"

                if e:
                    line1 += f"({a},{b}) -- "
                else:
                    line1 += f"({a},{b})    "

                if s:
                    line2 += "   |       "
                else:
                    line2 += "           "
            else:
                line1 += "           "
                line2 += "           "
        print(line1)
        print(line2)

level = populate_level(
    rooms=10,
    connections=11,
    empty_pct=10,
    empty_var=5,
    spread=2
) 

print(convert_to_seed(level))

printout(level, 17)
check_connections(level)