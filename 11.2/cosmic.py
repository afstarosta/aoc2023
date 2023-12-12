input = open('input.txt', 'r')
lines = input.readlines()
new_map = []
stars = {}
star_distance = {}
duplicated_lines = []
duplicated_columns = []

for i, line in enumerate(lines):
    line = line.replace('\n', '')
    lines[i] = line
    new_map.append(line)

for i, line in enumerate(lines):
    set_line = set(line)
    if len(set_line) == 1 and list(set_line)[0] == '.':
        duplicated_lines.append(i)
        
transposed_map = [[lines[j][i] for j in range(len(lines))] for i in range(len(lines[0]))]

for i, line in enumerate(transposed_map):
    set_line = set(line)
    if len(set_line) == 1 and list(set_line)[0] == '.':
        duplicated_columns.append(i)
        
print(duplicated_lines)
print(duplicated_columns)

star_counter = 1

for i, row in enumerate(new_map):
    for j, col in enumerate(row):
        if col == '#':
            new_map[i] = new_map[i].replace('#', str(star_counter), 1)
            
            l = i + sum(i > l for l in duplicated_lines) * (1000000 - 1)
            c = j + sum(j > c for c in duplicated_columns)  * (1000000 - 1)
            
            stars[str(star_counter)] = [l, c]
            star_distance[str(star_counter)] = {}
            star_counter += 1

for star in stars:
    for second_star in stars:
        if star == second_star:
            break
        if second_star not in star_distance[star]:
            c1 = stars[star]
            c2 = stars[second_star]
            distance = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
            star_distance[star][second_star] = distance
            star_distance[second_star][star] = distance

for s in star_distance:
    print(s)
    print(stars[s])
    print(star_distance[s])

for i in new_map:
    print(i)

acc = 0
for s in star_distance:
    for d in star_distance[s]:
        acc += star_distance[s][d]
print(acc//2)