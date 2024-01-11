"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def check_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True

palindrome_list = []

for i in range(100,1000):
    for j in range(100,1000):
        if check_palindrome(i*j):
            palindrome_list.append(i*j)

print(max(palindrome_list))