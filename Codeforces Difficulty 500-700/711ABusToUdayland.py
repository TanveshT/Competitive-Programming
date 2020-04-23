n = int(input())

resultList = []
flag = False
for _ in range(n):
    left, right = map(str, input().split('|'))
    if left == 'OO' and flag == False: 
        left = '++'
        flag = True
    elif right == 'OO' and flag == False:
        right = '++'
        flag = True
    resultList.append(left + '|' + right)

if flag:
    print('YES')
    for x in resultList:
        print(x)
else:
    print('NO')
