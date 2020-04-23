t = int(input())

result = []
for _ in range(t):

    a, b, c = map(int, input().split())
    result.append((a+b+c)//2)

for x in result:
    print(x)