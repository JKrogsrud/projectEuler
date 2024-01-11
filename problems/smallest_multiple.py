"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# This method works but takes like 45 seconds
"""
def lcm(x,y):
    if (x%y == 0) or (y%x == 0):
        return max(x,y)
    for i in range(1,x*y+1):
        if (i % x == 0) and (i % y == 0):
            return i

c_mult = 1
for i in range(1,21):
    print(i)
    c_mult = lcm(c_mult,i)

print(c_mult)
"""

# This one works much faster

lcm = 1
for k in (range(1, 21)):
    # Check if this new k ads something new
    print(k)
    if lcm % k > 0:
        # Now check the rest of this list to see if multiplying lcm by a later number gets the current number we are
        # interested in
        for j in range(1, 21):
            if (lcm*j) % k == 0:
                print(k)
                # When we see that this later number j manages to multiply lcm and doing so allows division by k we break
                lcm *= j
                break
print(lcm)


