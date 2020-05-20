t = int(input())
result = []

for _ in range(t):

    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(1, n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            count += 1
 
    result.append(count)

for i in range(t):
    print("Case #"+str(i+1)+":", result[i], sep = " ")