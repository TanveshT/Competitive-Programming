t = int(input())

result = []
for _ in range(t):
    a, b = map(int, input().split())
    dif = a-b
    if dif == 0: result.append(0)
    elif dif % 2 != 0:
        if dif < 0: result.append(1)
        else: result.append(2)
    else:
        if dif < 0: result.append(2)
        else: result.append(1)
    
for x in result:
    print(x)