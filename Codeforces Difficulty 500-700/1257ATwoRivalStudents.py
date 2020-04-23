t = int(input())

result = []
for _ in range(t):

    n, x, a, b = map(int, input().split())

    result.append(min(n-1, abs(a-b) + x))
for x in result:
    print(x)