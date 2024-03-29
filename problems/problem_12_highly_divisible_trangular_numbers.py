"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 +
 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import numpy as np

def num_factors(n):
    i = 1
    count = 0
    while i*i <= n:
        if n % i == 0:
            if n//i != i:
                count += 2
            else:
                count += 1
        i += 1
    return count

def triangular_sequence():
    num = 1
    n = 1
    while True:
        yield num
        num = num + n + 1
        n = n + 1

tri_gen = triangular_sequence()

factors = 1

while factors < 500:
    num = next(tri_gen)
    factors = num_factors(num)

print(num, factors)
