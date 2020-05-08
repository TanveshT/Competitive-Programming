t = int(input())

for _ in range(t):

    count = 0
    a, b, c = map(int, input().split())

    count += 3*min(c//2,b)
    b -= min(c//2,b)
    count += 3*min(a,b//2)
    print(count)