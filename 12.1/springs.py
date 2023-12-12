input = open('input.txt', 'r')
lines = input.readlines()

springs = []

for line in lines:
    values = [int(s) for s in line.split(' ')[1].split(',')]
    puzzle = line.split(' ')[0].replace('\n', '')
    springs.append({'values': values, 'puzzle': puzzle})


def rec(line, values):
    if '?' in line:
        return rec(line.replace('?', '#', 1), values) + rec(line.replace('?', '.', 1), values)
    elif is_valid_resolution(line, values):
        return 1
    else:
        return 0

def is_valid_resolution(line, values):
    clusters = line.split('.')
    clusters = list(filter(('').__ne__, clusters))
    if len(clusters) != len(values):
        return False
    for i, v in enumerate(values):
        if len(clusters[i]) != v:
            return False
    return True


acc = 0
for spring_line in springs:
    print(spring_line['puzzle'])
    acc += rec(spring_line['puzzle'], spring_line['values'])

print(acc)

