import math
input = open('input.txt', 'r')
lines = input.readlines()


races = []

times = ' '.join(lines[0].split(":")[1].split()).split(" ")
distances = ' '.join(lines[1].split(":")[1].split()).split(" ")

accumulator = 1

for i in range(len(times)):
    t = int(times[i])
    d = int(distances[i])
    min_value = -1
    max_value = -1

    for i in range(t):
        if (t - i) * i > d:
            min_value = i
            break

    for i in reversed(range(t)):
        if (t - i) * i > d:
            max_value = i
            break
            
    accumulator *= max_value - min_value + 1

print(accumulator)