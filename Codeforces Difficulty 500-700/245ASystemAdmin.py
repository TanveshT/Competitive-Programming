n = int(input())

aSuccess = 0
bSuccess = 0
aFail = 0
bFail = 0    

for _ in range(n):

    t, success, fail = map(int, input().split())

    if t == 1:
        aSuccess += success; aFail += fail
    else:
        bSuccess += success; bFail += fail

if aSuccess >= aFail: print('LIVE')
else: print('DEAD')

if bSuccess >= bFail: print('LIVE')
else: print('DEAD')