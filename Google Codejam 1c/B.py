t = int(input())
result = []

for i in range(t):

    x = {}
    a = []
    u = int(input())
    xSet = set()
    ySet = set()
    for j in range(10000):
        a.append(input().split())

    for j in a:
        xSet.update(set(j[1])) 
        if int(j[0][0]) == -1:
            continue 
        if len(j[0]) == len(j[1]):
            if j[1][0] not in x:
                x[j[1][0]] = 9
            ySet.add(int(j[0][0]))
            x[j[1][0]] = min(int(j[0][0]), x[j[1][0]])

    res = [''] * 10

    for k in x:
        res[x[k]] = k

    left = xSet - set(x.keys())

    for i in range(10):
        if res[i] == '':
            res[i] = left.pop()

    result.append(''.join(res))
        
for i in range(t):
    print("Case #"+str(i+1)+":", result[i], sep = " ")