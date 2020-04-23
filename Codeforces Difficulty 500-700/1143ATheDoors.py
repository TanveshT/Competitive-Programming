n = int(input())

arr = list(map(int, input().split()))

oneCount = 0
zeroCount = 0

for x in arr:
    if x == 0: zeroCount += 1
    else: oneCount += 1

count = 0
for x in arr:
    if x == 0: zeroCount -= 1
    else: oneCount -= 1
    count += 1
    if oneCount == 0 or zeroCount == 0: break

print(count)