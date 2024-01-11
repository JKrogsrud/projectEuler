i = 2
candidates = []
while i*i <= 600851475143:
    if 600851475143 % i == 0:
        candidates.append(i)
    i += 1

factors = []
for candidate in candidates:
    factors.append(int(600851475143/candidate))

factors = candidates + factors

for factor in factors:
    for other in factors[factors.index(factor)+1:]:
        if other % factor == 0:
            factors.remove(other)

print(max(factors))