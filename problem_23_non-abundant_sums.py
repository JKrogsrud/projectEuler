# Source: https://projecteuler.net/problem=23

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper
divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
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


def is_abundant(n):

    if sum(factors(n)) > n:
        return True

    else:
        return False


def is_abundant_sum(n):

    for i in range(1,n):
        if is_abundant(i) and is_abundant(n-i):
            return True
    return False


abundant_list =[]
for i in range(1, int(28123/2)):
    if is_abundant(i):
        abundant_list.append(i)


for i in range(1,28123):

print(len(abundant_list))