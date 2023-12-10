input = open('input.txt', 'r')
lines = input.readlines()

games = []

color_limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

accumulator = 0

for i, line in enumerate(lines):
    min_cubes = {'blue': 0, 'green': 0, 'red': 0}
    sets = line.split(':')[1].split(';')

    for cube_set in sets:
        colors = cube_set.split(',')
        for color in colors:
            color = color.strip()
            color_split = color.split(' ')
            color_quantity = int(color_split[0])
            color_name = color_split[1]

            if min_cubes[color_name] < color_quantity:
                min_cubes[color_name] = color_quantity
    power_guido = min_cubes['blue'] * min_cubes['green'] * min_cubes['red']
    accumulator += power_guido

print(accumulator)
    

