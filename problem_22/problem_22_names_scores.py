# Source: https://projecteuler.net/problem=22

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

file = open('names.txt')

for line in file:
    name_list = line.split(',')

name_list = [name[1:-1] for name in name_list]
name_list.sort()

scores = 0

for i in range(len(name_list)):
    alpha_value = 0
    for letter in name_list[i]:
        alpha_value += ord(letter) - 64
    name_score = alpha_value * (i+1)
    scores += name_score

print(scores)