n = int(input())

rank = 1
for i in range(n):
    a, b, c, d = map(int, input().split())

    total = a + b + c + d

    if i == 0:
        ThomasTotal = total
        continue

    if total > ThomasTotal:
        rank += 1
    
print(rank)
