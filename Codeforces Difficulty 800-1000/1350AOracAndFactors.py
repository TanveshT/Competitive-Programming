t = int(input())

for _ in range(t):

    n, k  = map(int, input().split())

    x = None
    for i in range(2,n//2):
        if n%i == 0:
            x = i
            break

    if x == None:
        x = n

    if x % 2 != 0:
        if k == 0:
            print(n)
        else:
            print(n+x + (2*(k-1)))
    else:
        print(n + 2*k)