t = int(input())

for _ in range(t):

    n = int(input())

    res = []
    i = 0
    while(n > 0):
        x = n%10
        if x != 0:
            res.append(x * (10**i))
        n //=10
        i += 1
    
    print(len(res))
    print(*res, sep = " ")