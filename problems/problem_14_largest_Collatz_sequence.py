# Source : https://projecteuler.net/problem=14

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# Result of pure brute force yields 837799 taking 525 iterations to complete, the process too 34.25 seconds to complete

import time

start = time.time()
def collatz_length(num):
    length = 1
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            length += 1
        else:
            num = (3 * num + 1)/2
            length += 2
    return length

max = 1
max_num = 1

for i in range(1,100):
    col_length = collatz_length(i)
    if col_length > max:
        max = col_length
        max_num = i

print(max_num, max)

print(f'This took {time.time()-start} seconds to complete')
