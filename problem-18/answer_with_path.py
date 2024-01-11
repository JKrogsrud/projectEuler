block = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

import copy

rows = block.split('\n')  # Break block into rows

pyramid = []

for row in rows:  # Break each row into a list of integers
    row = row.split(' ')
    int_row = []
    for entry in row:
        int_row.append(int(entry))
    pyramid.append(int_row)

pyramid_init = copy.deepcopy(pyramid)

for loc in range(len(pyramid[-1])):
    pyramid[-1][loc] = [pyramid[-1][loc], [(len(pyramid)-1,loc)]]

def row_reduce(pyramid):
    if len(pyramid)==1:
        return pyramid
    for loc in range(len(pyramid[-2])):
        if pyramid[-1][loc][0] >= pyramid[-1][loc+1][0]:
            journey = copy.copy(pyramid[-1][loc][1])
            journey.append((len(pyramid)-2,loc))
            pyramid[-2][loc] = [pyramid[-2][loc]+pyramid[-1][loc][0], journey]
        else:
            journey = copy.copy(pyramid[-1][loc+1][1])
            journey.append((len(pyramid)-2,loc))
            pyramid[-2][loc] = [pyramid[-2][loc] + pyramid[-1][loc+1][0], journey]
    pyramid = pyramid[:-1]
    return(row_reduce(pyramid))

new_pyramid = row_reduce(pyramid)

print(f'The maximized route sums to {new_pyramid[0][0][0]} and the journey it took was {new_pyramid[0][0][1][::-1]}')

for row in range(len(pyramid_init)):
    line = ''
    for pos in range(len(pyramid_init[row])):
        if (row, pos) in new_pyramid[0][0][1][::-1]:
            line = line + f' _{pyramid_init[row][pos]}_ '
        else:
            line = line + f' {pyramid_init[row][pos]} '
    print(line)