n = int(input())

capacity = 0
current = 0
for _ in range(n):

    a, b = map(int, input().split())

    current += b
    current -= a

    capacity = max(capacity, current)

print(capacity)