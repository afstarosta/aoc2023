def find_location_from_seed(seed):
    seed = str(seed)
    seeds = {}
    seeds[seed] = {'seed': int(seed)}
    has_found_location = False
    last_step = 'seed'
    last_value = 0
    while has_found_location == False:
        current_conversion = maps[last_step]
        target = current_conversion['to']
        if target == 'location':
            has_found_location = True
        seeds[seed][target] = seeds[seed][last_step]
        for rule in current_conversion['rules']:
            if rule['start']  <= seeds[seed][last_step] <= rule['end']:
                seeds[seed][target] = seeds[seed][last_step] + rule['conversion']
                break
        last_step = target
    return seeds[seed]['location']


input = open('input.txt', 'r')
lines = input.readlines()

maps = {}
current_source = ''
seeds_input_line = ''

for line in lines:
    if 'seeds:' in line:
        seeds_input_line = list(map(int, line.split(':')[1].strip().split(' ')))

    if line == '\n':
        is_reading = False
        current_source = ''
    
    if 'map:' in line:
        is_reading = True
        current_source = line.split(' ')[0].split('-to-')[0]
        map_target = line.split(' ')[0].split('-to-')[1]
        maps[current_source] = {}
        maps[current_source]['to'] = map_target
    
    if line[0].isdigit():
        rules = list(map(int,line.split(' ')))
        rule_dict = {
                'start': rules[1],
                'end': rules[1] + (rules[2] - 1),
                'conversion': rules[0] - rules[1],
                'target': rules[0],
                'range': rules[2]
            }
        if 'rules' in maps[current_source]:
            maps[current_source]['rules'].append(rule_dict)
        else:
            maps[current_source]['rules'] = [rule_dict]



seeds = []
for i in range(0, len(seeds_input_line) - 1, 2):
    seeds.append([seeds_input_line[i], seeds_input_line[i] + seeds_input_line[i + 1] - 1])

ranges_to_process = seeds
similar_areas = []

while len(ranges_to_process) != 0:
    x, y = ranges_to_process.pop()
    previous_y = y

    while find_location_from_seed(x) - x != find_location_from_seed(y) - y:
        y = (x + y)//2

    similar_areas.append([x, y])

    if previous_y > y:
        ranges_to_process.append([y+1, previous_y])

print(min([find_location_from_seed(i[0]) for i in similar_areas]))
