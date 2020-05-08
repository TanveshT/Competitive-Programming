t = int(input())

result=[]
for _ in range(t):
    
    n, b = map(int, input().split())
    a = list(map(int, input().split()))

    a = sorted(a)
    count = 0
    cost = 0

    for x in a:
        cost += x
        if cost > b: break
        count += 1

    result.append(count)

for i in range(t):
    print("Case #"+str(i+1)+":", result[i], sep = " ")