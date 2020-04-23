t = int(input())
result = []

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    oddFlag = False
    evenFlag = False

    for x in a:
        if x%2==0: evenFlag = True
        else: oddFlag = True
        if evenFlag and oddFlag: break

    if oddFlag == False or (evenFlag == False and n%2==0):
        result.append('NO')
    else:
        result.append('YES') 

for x in result:
    print(x)