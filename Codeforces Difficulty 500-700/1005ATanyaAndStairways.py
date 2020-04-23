n = int(input())
arr = [9999] + list(map(int, input().split()))
arr += [0]

countStairways = 0
result = []
count = 1
for i in range(1,n+2):
    if arr[i-1] >= arr[i]:
        countStairways += 1
        result.append(arr[i-1])
       

print(countStairways-1)
for i in range(1,countStairways):
    print(result[i],end = " ")
