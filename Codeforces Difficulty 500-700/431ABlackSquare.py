arr = list(map(int, input().split()))
s = input()
count = 0
for x in s:
    count += arr[int(x) - 1]
print(count)