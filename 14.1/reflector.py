input = open('input.txt', 'r')
lines = input.readlines()

transposed_lines = [[lines[j][i] for j in range(len(lines))] for i in range(len(lines[0]))]
transposed_lines.pop()


for i, line in enumerate(transposed_lines):
    a = ''.join(line)
    transposed_lines[i] = '#'.join([''.join(sorted(q, reverse=True)) for q in a.split('#')])

acc = 0
for line in transposed_lines:
    for i, char in enumerate(line):
        if char == 'O':
            acc += len(line) - i

print(acc)