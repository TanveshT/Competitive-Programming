t = int(input())

for _ in range(t):

    n = int(input())
    arr = list(map(int, input().split()))

    x = [0] * (n+1)

    for i in arr:
        x[i] = 1
    
    for i in range(1, n+1):
        if x[i] == 0:
            print(i)
            break