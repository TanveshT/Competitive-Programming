t = int(input())
result = []

for i in range(t):

    n, d = map(int, input().split())
    x = list(map(int, input().split()))

    l = d
    for i in range(n-1,-1,-1):
        l = l - l%x[i]

    result.append(l)

for i in range(t):
    print("Case #"+str(i+1)+":", result[i], sep = " ")