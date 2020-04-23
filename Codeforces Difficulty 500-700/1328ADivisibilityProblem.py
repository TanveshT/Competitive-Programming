t = int(input())
result = []

for _ in range(t):

    a, b = map(int, input().split())
    x = a % b
    if x == 0: result.append(0)
    else: result.append(b - x)

for x in result:
    print(x)