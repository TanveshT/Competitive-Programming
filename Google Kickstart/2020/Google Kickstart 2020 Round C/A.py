t = int(input())
result = []

for _ in range(t):

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    mainCount = 0
    count = 0
    flag = False
    prev = None
    for i in range(n):
        if flag and prev != None:
            if prev - a[i] == 1:
                count += 1
                prev = a[i]
            else:
                count = 0
                prev = None
        if a[i] == k:
            flag = True
            count += 1
            prev = a[i]
        if count == k:
            mainCount += 1

    result.append(mainCount)

for i in range(t):
    print("Case #"+str(i+1)+":", result[i], sep = " ")