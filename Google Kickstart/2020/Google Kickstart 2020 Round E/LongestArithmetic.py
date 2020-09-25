t = int(input())
result = []

for _ in range(t):

    n = int(input())
    arr = list(map(int, input().split()))
    diffArr = [0] * n

    for i in range(1,n):
        diffArr[i] = arr[i-1] - arr[i]

    maxConsecutive = 0
    temp = 0
    for i in range(1, n):
        if i == (n-1):
            break
        if diffArr[i+1] == diffArr[i]:
            temp+=1
            maxConsecutive = max(temp, maxConsecutive)
        else:
            temp = 0

    result.append(maxConsecutive+2)

for i in range(t):
    print("Case #"+str(i+1)+":", result[i], sep = " ")