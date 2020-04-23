t = int(input())
result = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    even = 0
    odd = []
    oddCount = 0

    flag = False
    for i in range(n):
        if arr[i]%2==0:
            flag = True
            result.append([i+1])
            break
        elif oddCount != 2:
            oddCount += 1
            odd.append(i+1)
            if oddCount == 2: 
                flag = True
                result.append(odd)
                break
    
    if not flag:
        result.append(-1)

            
for x in result:
    if x == -1:
        print(x)
        continue
    print(len(x))
    for y in x:
        print(y, end = " ")
    print()