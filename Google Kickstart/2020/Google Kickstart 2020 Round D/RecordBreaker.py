t = int(input())
result = []

for _ in range(t):

    n = int(input())
    arr = list(map(int, input().split()))

    maxTillNow = 0
    count = 0

    for i in range(n-1):
        if arr[i] > maxTillNow and arr[i] > arr[i+1]:
            count+=1
        maxTillNow = max(maxTillNow, arr[i])

    if arr[n-1] > maxTillNow: count+=1
    result.append(count)

for i in range(t):
    print("Case #"+str(i+1)+":", result[i], sep = " ")
