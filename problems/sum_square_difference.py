square_sums = 0
for i in range(1,101):
    square_sums += i**2

sums_squared = (100*101/2)**2

print(sums_squared - square_sums)