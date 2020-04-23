n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

count = 0
result = []
for x in range(1,m+1):
    flag = True
    for y in arr:
        if x>= y[0] and x <= y[1]:
            flag = False
            break
    if flag:
        count += 1
        result.append(x)

print(count)
for x in result:
    print(x, end  = " ")
