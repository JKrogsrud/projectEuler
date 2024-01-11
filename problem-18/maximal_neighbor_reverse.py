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

# Let's cycle through the entire last line as a starting point
max_sum = 0

for end in range(len(pyramid[-1])):

    row = len(pyramid) - 1  # Always start at last row
    position = end
    sum = pyramid[row][position]  # Start sum as the starting positions value

    while row > 0: # Calculate the sum of route
        #print(row, position)
        # Allow choice to be made if we are not at position of 0.
        if position > 0:
            if position == row:
                position -= 1
            elif pyramid[row-1][position-1] > pyramid[row-1][position]:
                position -= 1
        sum += pyramid[row][position]
        row -= 1
    print(sum)
    if sum > max_sum:
        max_sum = sum

print(max_sum)

#  Definitely not the largest either, 919
