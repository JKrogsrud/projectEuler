fibon0 = 1
fibon1 = 2
sum = 2

while fibon0 + fibon1 < 4000000:
    fibon_next = fibon0 + fibon1
    if fibon_next % 2 == 0:
        sum += fibon_next
    fibon0 = fibon1
    fibon1 = fibon_next

print(sum)