import numpy as np
import time

start = time.time()
primes = np.arange(0,2000001,1)
primes[1] = 0

for prime in primes:
    if prime != 0:
        discard_index = 2 * prime
        while discard_index < len(primes):
            primes[discard_index] = 0
            discard_index += prime

#arr = arr.astype('float64')
print(time.time()-start)
actual_primes = primes[primes != 0].astype('int64')
#print(len(actual_primes))
print(len(actual_primes))