t = int(input())

result = []
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    result.append(min(arr[0] + sum(arr[1:n]), m))

for x in result:
    print(x)