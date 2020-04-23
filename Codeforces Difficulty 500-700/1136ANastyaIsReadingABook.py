n = int(input())

arr = [] 

for _ in range(n):
    arr.append(list(map(int,input().split())))

k = int(input())

count = 0

for x in arr:
    if k <= x[1]:
        break
    count += 1

print(n-count)