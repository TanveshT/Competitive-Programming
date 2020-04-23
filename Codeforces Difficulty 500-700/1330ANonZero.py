t = int(input())

result = []
for _ in range(t):

    n = int(input())
    arr = list(map(int, input().split()))

    countZero = 0
    sumArr = 0
    for x in arr:
        sumArr += x
        if x==0: countZero += 1

    count = 0
    count += countZero
    sumArr += count

    if sumArr == 0:
        count += 1

    result.append(count)

for x in result:
    print(x)