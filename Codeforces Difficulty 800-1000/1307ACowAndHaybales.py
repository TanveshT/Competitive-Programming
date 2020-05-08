t = int(input())

for _ in range(t):

    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(1,n):
        boxAdd = (min(a[i]*i, d)//i)
        a[0] += boxAdd
        d -= boxAdd * i

    print(a[0])