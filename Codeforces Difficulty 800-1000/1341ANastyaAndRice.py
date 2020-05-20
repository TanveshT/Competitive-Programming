t = int(input())

for _ in range(t):

    n, a, b, c, d = map(int, input().split())

    lowBGrain = n*(a - b)
    highBGrain = n*(a + b)

    lowBPackage = c - d
    highBPackage = c + d

    if highBGrain < lowBPackage or highBPackage < lowBGrain:
        print('No')
    else:
        print('Yes')