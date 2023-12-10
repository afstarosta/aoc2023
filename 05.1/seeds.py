input = open('input.txt', 'r')
lines = input.readlines()

seeds = {}
maps = {}

current_source = ''

for line in lines:
    
    if 'seeds:' in line:
        seeds_input = line.split(':')[1].strip().split(' ')
        for seed in seeds_input:
            seeds[seed] = {'seed': int(seed)}

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

min_location = -1
for seed in seeds:
    has_found_location = False
    last_step = 'seed'
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

    location = seeds[seed]['location']
    if min_location == -1:
        min_location = location
    else:
        if location < min_location:
            min_location = location

print(min_location)
