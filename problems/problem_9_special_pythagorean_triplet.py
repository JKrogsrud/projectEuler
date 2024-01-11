import numpy as np
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.
"""
def find_triplet():
    for b in range(1,1000):
        a = (1000000-2000*b)/(2000-2*b)
        if (a > 0) and int(a) == a:
            return(a,b)

a, b = find_triplet()
c = np.sqrt((a**2) + (b**2))

print(a*b*c)