n = int(input())
arr = list(map(int, input().split()))
maxValue = max(arr)
count = 0
for x in arr:
    count += (maxValue - x)
print(count)