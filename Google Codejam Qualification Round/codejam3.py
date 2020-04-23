t=int(input())

resultList=[]

for _ in range(t):
    ans=""
    n=int(input())
    times=[]
    
    available=[0]*2
    for i in range(n):
        toappend=[0]*2
        pair=list(map(int,input().split()))
        toappend[0],toappend[1] = i,pair
        times.append(toappend)

    times=sorted(times,key=lambda x:x[1][0])

    for i in range(n):
        if available[0]<= times[i][1][0]:
            available[0] = times[i][1][1]
            ans='C'

        elif available[1]<= times[i][1][0]:
            available[1] = times[i][1][1]
            ans='J'
   
        else:
            ans="IMPOSSIBLE"
            times[i][1]=ans
            break
        times[i][1]=ans

    result=""
    times=sorted(times,key=lambda x:x[0])
    for i in range(n):
        if str(times[i][1])=="IMPOSSIBLE":
            result=times[i][1]
            break
        result+=str(times[i][1])
    resultList.append(result)

for i in range(t):
    print("Case #"+str(i+1)+":", resultList[i], sep = " ")
