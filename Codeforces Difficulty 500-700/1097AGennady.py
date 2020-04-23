onTable = input()
inHand = '' .join(input().split())
if onTable[0] in inHand or onTable[1] in inHand:
    print('YES')
else:
    print('NO')