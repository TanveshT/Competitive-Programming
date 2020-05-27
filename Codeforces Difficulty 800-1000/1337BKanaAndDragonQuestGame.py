import math

t = int(input())

for _ in range(t):

    h, n, m = map(int, input().split())
    count = 0

    while(h > 0 and n > 0 and (h//2+10) < h):
        n-=1
        h = h//2 + 10

    if h <= m*10:
        print('YES')
    else:
        print('NO')
