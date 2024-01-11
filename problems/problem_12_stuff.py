import numpy as np
import time


primes = np.arange(0,100,1)
primes[1] = 0

for prime in primes:
    if prime != 0:
        discard_index = 2 * prime
        while discard_index < len(primes):
            primes[discard_index] = 0
            discard_index += prime


actual_primes = primes[primes != 0].astype('int64')

print(actual_primes[:22])

num = 1
for i in actual_primes[:22]:
    num = num * (i**2)

print(num)

k = num * (2*num +1)
print(k)