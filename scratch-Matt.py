{
    '1': {
        'id': 1,
        'coord_x': 0,
        'coord_y': 0,
        'north': 5,
        'south': 0,
        'east': 0,
        'west': 2
    },
    '2': {
        'id': 2,
        'coord_x': -1,
        'coord_y': 0,
        'north': 6,
        'south': 3,
        'east': 1,
        'west': 0
    },
    '3': {
        'id': 3,
        'coord_x': -1,
        'coord_y': -1,
        'north': 2,
        'south': 0,
        'east': 0,
        'west': 4
    },
    '4': {
        'id': 4,
        'coord_x': -2,
        'coord_y': -1,
        'north': 0,
        'south': 0,
        'east': 3,
        'west': 0
    },
    '5': {
        'id': 5,
        'coord_x': 0,
        'coord_y': 1,
        'north': 0,
        'south': 1,
        'east': 0,
        'west': 6
    },
    '6': {
        'id': 6,
        'coord_x': -1,
        'coord_y': 1,
        'north': 0,
        'south': 2,
        'east': 5,
        'west': 0
    },
}

graph_width = (int)
graph_height = (int)

multiplier = (int)

root_x = graph_width // 2
root_y = graph_height // 2

cx = multiplier*node_x + root_x
cy = multiplier*node_y + root_y
