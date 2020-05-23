from math import ceil

t = int(input())

for _ in range(t):

    a, b, c, d = map(int, input().split())

    if b >= a:
        print(b)
    elif c <= d:
        print(-1)
    else:
        diff = a-b
        print(ceil(diff/(c-d))*c + b)
        
