# Source : https://projecteuler.net/problem=18

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top
to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
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
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67,
is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force,
and requires a clever method! ;o)
"""

# Without anything more clever let's try some of the traveling salesmen algorithms. First being largest neighbor.
# Start by converting our triangle to something workable

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

rows = block.split('\n')  # Break block into rows

pyramid = []

for row in rows:  # Break each row into a list of integers
    row = row.split(' ')
    int_row = []
    for entry in row:
        int_row.append(int(entry))
    pyramid.append(int_row)

# Let's start with a simple maximal neighbor strategy

position = 0  # position will be the location we are in a given row of the pyramid, starting at 0
row = 0  # Row will be the current row, starting at 0

sum = pyramid[row][position]
print(row, position)
while row < len(pyramid)-1:
    if pyramid[row+1][position] < pyramid[row+1][position+1]:
        position += 1
    row += 1
    print(row, position)
    sum += pyramid[row][position]

print(sum)

# Didn't end up as maximal, oh well, I really didn't think it would
# Result 1064