def prime_factorise(x):
    dic = {}
    n = 2
    while n<=x:
        cnt = 0
        if n==2:
            while x%n ==0 and x>=n:
                cnt+=1
                x = x/n
            if cnt>=1:
              dic[str(n)] = cnt
            n+=1
        else:
                while x%n ==0 and x>=n:
                    cnt+=1
                    x = x/n
                if cnt>=1:
                  dic[str(n)] = cnt
                n+=2
    return (dic)
n = 1
no_divisor = 1
while no_divisor<=500:
    sum_ = n*(n+1)/2
    temp = 1
    for value in prime_factorise(sum_).values():
        temp*= (value+1)
    no_divisor = temp
    n+=1
print(sum_)