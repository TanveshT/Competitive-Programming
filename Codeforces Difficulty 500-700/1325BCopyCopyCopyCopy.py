t = int(input())

result = []
for _ in range(t):

    n = int(input())
    arr = list(map(int, input().split()))

    arr = set(arr)
    result.append(len(arr))

for x in result:
    print(x)