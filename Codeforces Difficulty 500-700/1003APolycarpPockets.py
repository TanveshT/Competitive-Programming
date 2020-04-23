n = int(input())
arr = list(map(int, input().split()))

countArr = [0] * 101
for i in range(n):
    countArr[arr[i]] += 1

print(max(countArr))