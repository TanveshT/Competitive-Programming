import math

t = int(input())

for _ in range(t):

    h, n, m = map(int, input().split())
    x = 10*m
    flag = False
    for i in range(n):
        if math.floor(((h/(2**i)) + (20*(1-((1/2)**(i+1))))) -  x) <= 0:
            flag = True
            break

    if flag:
        print('YES')
    else:
        print('NO') 