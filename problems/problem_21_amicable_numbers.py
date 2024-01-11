# Source: https://projecteuler.net/problem=21

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def factors(n):
    i = 2
    factors = []
    while i*i <= n:
        if n % i == 0:
            if n//i != i:
                factors.append(i)
                factors.append(int(n / i))
            else:
                factors.append(i)
        i += 1
    factors.append(1)
    return factors

def is_amicable(n):
    possible_pair = sum(factors(n))
    if sum(factors(possible_pair)) == n and possible_pair != n:
        return True
    else:
        return False

amicables = []

for i in range(1, 10001):
    if is_amicable(i):
        amicables.append(i)

print(sum(amicables))