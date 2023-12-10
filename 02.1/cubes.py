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
    games.append({'blue': 0, 'green': 0, 'red': 0})
    sets = line.split(':')[1].split(';')
    valid = True
    for cube_set in sets:
        colors = cube_set.split(',')
        for color in colors:
            color = color.strip()
            color_split = color.split(' ')
            color_quantity = int(color_split[0])
            color_name = color_split[1]
            if color_limits[color_name] < color_quantity:
                valid = False
    if valid:
        accumulator += i+1

print(accumulator)