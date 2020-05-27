t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(a)

    minV = 99999
    for i in range(1,n):
        minV = min(minV , a[i] - a[i-1])

    print(minV)