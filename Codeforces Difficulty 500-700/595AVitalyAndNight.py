n, m = map(int, input().split())
m2 = 2*m
count = 0
for i in range(n):
    floor = list(map(int, input().split()))

    for j in range(0,m2,2):
        if floor[j] == 1 or floor[j+1] == 1:
            count += 1

print(count)