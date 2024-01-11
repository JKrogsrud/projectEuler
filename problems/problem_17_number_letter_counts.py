# Source: https://projecteuler.net/problem=17

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

# Make a dictionary that will translate some of the numbers i will encounter to text.
# Need teens, singletons and all the ____ty's, leave 0 as blank as we don't pronounce it

int_to_text = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
}

# the following should take a number and count how many letters are used without needing to actually string it together

def lettercount(number):
    count = 0
    # Find the number in thousands space, hundreds, tens and digits.
    thousands = (number // 1000) % 10
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    digits = number % 10

    # First exception should be the teens, if tens == 1
    if tens == 1:
        count += len(int_to_text[number % 100])  # Count length of the teens spelled out, from 'ten' to 'nineteen'

    if tens !=1:  # So long as the tens space is not 1 we will be adding the length of the digit word
        count += len(int_to_text[tens * 10])  # takes the tens digit, multiplies it by 10 to look up in the dictionary
        count += len(int_to_text[digits])  # looks up the digits

    if hundreds != 0:  # Adds 'hundred' 'and' to our word

        if digits == 0 and tens == 0:  # Except when we first hit a new hundred as we don't say 'and zero'

            count += len(int_to_text[hundreds]) + len('hundred')

        else:

            count += len(int_to_text[hundreds]) + len('hundred') + len('and')

    if thousands != 0:  # We only are going to hit 1000 and nothing more but this should work to 10000

        count += len(int_to_text[thousands]) + len('thousand')

    return count


big_count = 0

for i in range(1, 1001):
    big_count += lettercount(i)

print(big_count)