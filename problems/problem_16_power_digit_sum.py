# source: https://projecteuler.net/problem=16

"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

answer = str(2**1000)
print(answer)

sum = 0

for num in range(len(answer)):
    sum += int(answer[num])

print(sum)