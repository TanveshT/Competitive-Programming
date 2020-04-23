n = int(input())
arr = list(map(int, input().split()))

resultArr = [0] * (n+1)
for i in range(n):
    resultArr[arr[i]] = i + 1

for i in range(1,n+1):
    print(resultArr[i], end = " ")