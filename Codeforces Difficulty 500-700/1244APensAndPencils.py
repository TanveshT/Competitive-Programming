import math
t = int(input())

result = []
for _ in range(t):

    a, b, c, d, k = map(int, input().split())

    pensRequired = math.ceil(a/c)
    pencilsRequired = math.ceil(b/d)

    if pensRequired + pencilsRequired <= k:
        result.append((pensRequired, pencilsRequired))
    else:
        result.append(-1)

for x in result:
    if x == -1:
        print(x)
    else:
        print(x[0], x[1], sep = " ")