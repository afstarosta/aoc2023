input = open('input.txt', 'r')
lines = input.readlines()

for i, line in enumerate(lines):
    lines[i] = line.replace('\n', '')


def rotate_matrix_cc( m ):
    return [[lines[j][i] for j in range(len(lines))] for i in range(len(lines[0])-1,-1,-1)]


def rotate_matrix_c(m):
    return [list(reversed(col)) for col in zip(*m)]

def roll_to_left(m):
    for i, line in enumerate(m):
        a = ''.join(line)
        m[i] = '#'.join([''.join(sorted(q, reverse=True)) for q in a.split('#')])
    return m

def evaluate_matrix(m):
    acc = 0
    for line in m:
        for i, char in enumerate(line):
            if char == 'O':
                acc += len(line) - i
    return acc

def print_matrix(m):
    for l in m:
        print(' '.join(l))
    print()

# cycles = 10
# m = lines

# for i in range(cycles):
#     print_matrix(m)
#     m = rotate_matrix(m)
#     roll_to_left(m)
#     m = rotate_matrix(m)
#     roll_to_left(m)
#     m = rotate_matrix(m)
#     roll_to_left(m)
#     m = rotate_matrix(m)
#     roll_to_left(m)

#     print(str(cycles) + " -> " + str(evaluate_matrix(m)))

m = rotate_matrix_cc(lines)
results = []

offset = []
cycle = []

cycles = 100

for i in range(cycles):
    m = roll_to_left(m) # N
    
    m = rotate_matrix_c(m) # W
    m = roll_to_left(m)

    m = rotate_matrix_c(m) # S
    m = roll_to_left(m)
    
    m = rotate_matrix_c(m) # E
    m = roll_to_left(m)

    m = rotate_matrix_c(m) # N

    results.append(str(evaluate_matrix(m)))

print(results)