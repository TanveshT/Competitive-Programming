t = int(input())

result = []
for _ in range(t):

    a, b, k = map(int, input().split())

    if k%2 != 0: 
        result.append((a*(k//2+1)-(b*(k//2))))
    else:
        result.append((a-b)*(k//2))

for x in result:
    print(x)