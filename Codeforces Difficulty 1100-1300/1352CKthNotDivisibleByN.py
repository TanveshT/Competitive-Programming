t = int(input())

for _ in range(t):

    n, k = map(int, input().split())
    
    x = k%(n-1)
    y = k//(n-1)

    an = n*y

    if x == 0:
        print(an+x-1)
    else:
        print(an+x)