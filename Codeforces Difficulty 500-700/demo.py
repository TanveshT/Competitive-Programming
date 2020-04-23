t = int(input())
resultList = []

for _ in range(t):
    result = ''
    times = []
    cAvail = []
    jAvail = []
    n = int(input())
    for _ in range(n):
        times.append(list(map(int, input().split())))
        
    sortedTimes = sorted(times, key = lambda x: x[0])

    result += 'C'; cAvail.append(sortedTimes[0])
    result += 'J'; jAvail.append(sortedTimes[1])

    for i in range(2, n):
        
        cFlag = True
        jFlag = True
        for x in cAvail:
            if sortedTimes[i][0] in range(x[0], x[1]) or (sortedTimes[i][1]-1) in range(x[0], x[1]):
                cFlag = False
                break
        for x in jAvail:
            if sortedTimes[i][0] in range(x[0], x[1]) or (sortedTimes[i][1]-1) in range(x[0], x[1]):
                jFlag = False
                break

        if cFlag and jFlag: result += 'C'
        elif cFlag and not jFlag: result += 'C'
        elif jFlag and not cFlag: result += 'J'
        else: result = 'IMPOSSIBLE'; break

    indexes = sorted(range(len(times)), key=lambda k: times[k][0])

    if result != 'IMPOSSIBLE':
        for x in result:
            

    resultList.append(result)

for i in range(t):
    print("Case #"+str(i+1)+":", resultList[i], sep = " ")


