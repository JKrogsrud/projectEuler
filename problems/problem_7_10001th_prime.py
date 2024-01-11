def infinite_sequence():
    num = 2
    while True:
        yield num
        num += 1

gen = infinite_sequence()

prime_list = [2]
counter = 1

# Start a loop that will iterate only when the next prime is found

def is_new_prime(prime_list, number):
    for prime in prime_list:
        if number % prime == 0:
            return False
    return True

while counter < 10001:
    poss_p = next(gen)
    if is_new_prime(prime_list, poss_p):
        prime_list.append(poss_p)
        counter += 1

print(prime_list[-1])