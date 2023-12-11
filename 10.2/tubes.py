from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import matplotlib.pyplot as plt

input = open('input.txt', 'r')
map = input.readlines()
map = [line.replace('\n', '') for line in map]
loop_coords = []
points_inside_loop = []
cloned_map = [['I' for j in map[0]] for i in map]

dim = [len(cloned_map)- 1, len(cloned_map[0])- 1]


ortogonal_directions = [[0, 1], [0, -1], [1, 0], [1, 1], [1, -1], [-1, 0], [-1, 1], [-1, -1]]

directions = {
    'S': [1, 0], 
    'N': [-1, 0], 
    'E': [0, 1], 
    'W': [0, -1]
    }

direction_inversion = {
    'E': 'W',
    'W': 'E',
    'S': 'N',
    'N': 'S'
}

start_marker = 'S'

pipe_connections = {
    '|': {'N': 'S', 'S': 'N'},
    '-': {'W': 'E', 'E': 'W' },
    'L': {'N': 'E', 'E': 'N' },
    'J': {'N': 'W', 'W': 'N' },
    '7': {'S': 'W', 'W': 'S' },
    'F': {'S': 'E', 'E': 'S' },
}

starting_position = []
for i, line in enumerate(map):
    for j, char in enumerate(line):
        if char == start_marker:
            starting_position = [i, j]
            break
    if starting_position != []:
        break

cloned_map[starting_position[0]][starting_position[1]] = 'X'

def get_valid_neighbors(position, map):
    neighbors = []
    for direction in ['S', 'W', 'E', 'N']:
        transformation = directions[direction]
        target = [position[0] + transformation[0], position[1] + transformation[1]]
        if 0 <= target[0] <= len(map) -1 and 0 <= target[1] <= len(map[target[0]]) - 1:
            pipe_type = map[target[0]][target[1]]
            if pipe_type in pipe_connections and direction_inversion[direction] in pipe_connections[pipe_type]:
                neighbors.append([direction, target, pipe_type])
    return neighbors

def print_map(map):
    f = open("output.txt", "w")
    for line in map:
        print(line)
        f.write(''.join(line) + '\n')
         
valid_neighbors = get_valid_neighbors(starting_position, map)

current_position = valid_neighbors[0][1]
last_direction = valid_neighbors[0][0]
last_pipe_type = valid_neighbors[0][2]
loop_coords.append((starting_position[0], starting_position[1]))

while current_position != starting_position:
    loop_coords.append((current_position[0], current_position[1]))
    direction_inverted = direction_inversion[last_direction]
    next_direction = pipe_connections[last_pipe_type][direction_inverted]
    transformation = directions[next_direction]
    target = [current_position[0] + transformation[0], current_position[1] + transformation[1]]
    cloned_map[target[0]][target[1]] = 'X'

    last_pipe_type = map[target[0]][target[1]]
    last_direction = next_direction
    
    current_position = target


accumulator = 0
polygon = Polygon(loop_coords)
x,y = polygon.exterior.xy
plt.plot(x,y)
for i, line in enumerate(cloned_map):
    for j, char in enumerate(line):
        if char != 'X':
            point = [i, j]
            poly_point = Point(point[0], point[1])

            if poly_point.within(polygon):
                plt.plot([point[0]], [point[1]], 'o', color='green')
                accumulator += 1
            else:
                plt.plot([point[0]], [point[1]], 'o', color='red')
    
plt.show()
    
print(accumulator)
