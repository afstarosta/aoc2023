input = open('input.txt', 'r')
lines = input.readlines()

data = []

for line in lines:
    data.append([[int(s) for s in line.strip().split(' ')]])

for row_index, row in enumerate(data):
    has_finished = False
    current_row = row[0]
    while not has_finished:
        next_row = []
        for i in range(1, len(current_row)):
            next_row.append(current_row[i] - current_row[i - 1])
        data[row_index].append(next_row)
        current_row = next_row
        has_finished = all(v == 0 for v in current_row)


accumulator = 0

for row_index, row in enumerate(data):
    finished = False
    i = len(row) - 2
    while not finished:
        data[row_index][i].append(data[row_index][i][-1] + data[row_index][i + 1][-1])
        i -= 1
        finished = i == -1
    accumulator += data[row_index][0][-1]


for d in data:
    for p in d:
        print(p)
    print("\n")



print(accumulator)