def infinite_sequence():
    num = 3
    while True:
        yield num
        num += 2

prime_list = [2,3]

num_gen = infinite_sequence()

def is_new_prime(prime_list, number):
    for prime in prime_list:
        if number % prime == 0:
            return False
    return True

sum = 5
while prime_list[-1] < 2000000:
    poss = next(num_gen)
    if (poss % 6 == 1) or (poss % 6 == 5):
        if is_new_prime(prime_list, poss):
            #print(poss)
            sum += poss
            prime_list.append(poss)

sum = sum - prime_list[-1]
print(f'Sum is {sum}')