t = int(input())

resultList = []
for _ in range(t):
    result = ''
    n = input()
    previous = None
    opened = 0
    for x in n:
        if previous == None:
            result += '('*int(x) + x 
            previous = x
            opened = int(x)
        elif previous > x:
            result += ')' * (int(previous) - int(x)) + x
            opened -= (int(previous) - int(x))
            previous = x
        elif previous == x:
            result += x
            previous = x
        else:
            result += '(' * (abs(opened - int(x))) + x 
            opened += (abs(opened - int(x)))
            previous = x

    result+=(opened*')')
    resultList.append(result)

for i in range(t):
    print("Case #"+str(i+1)+":", resultList[i], sep = " ")


