t = int(input())

result = []

for _ in range(t):

    minute = 0
    x, y, m = input().split()
    x = int(x)
    y = int(y)

    flag = False

    if x + y == minute:
        flag = True

    for i in m:

        if flag == True:
            break

        minute += 1

        if i == 'N':
            y+=1
        elif i == 'S':
            y-=1
        elif i == 'E':
            x+=1
        else:
            x-=1

        if abs(x)+abs(y) <= minute:
            flag = True
            break

    if flag:
        result.append(minute)
    else:
        result.append('IMPOSSIBLE')

for i in range(t):
    print("Case #"+str(i+1)+":", result[i], sep = " ")