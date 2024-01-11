# Result of pure brute force yields 837799 taking 525 iterations to complete, the process too 34.25 seconds to complete

import time
import numpy as np

start = time.time()

collatz_dict = {}

def collatz_length(num):
    length = 1
    if num in collatz_dict:
        length += collatz_dict[num]
        return length
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            length += 1
        else:
            num = (3 * num + 1)/2
            length += 2
    return length

max = 0
max_num = 0

for i in range(1,1000000):
    length = collatz_length(i)
    if length > max:
        max = length
        max_num = i
    collatz_dict[i] = length
print(max, max_num)
print(f'This took {time.time()-start} seconds to complete')