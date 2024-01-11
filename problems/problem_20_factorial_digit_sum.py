# Source: https://projecteuler.net/problem=20

"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

fact_list = []

mult = 1
for i in range(2, 101):
    mult *= i


#test = 123456789123456789
for i in range(0,250):
    #print((mult // 10**i) % 10)
    fact_list.append((mult // 10**i) % 10)

print(fact_list)
sum = sum(fact_list)
print(sum)