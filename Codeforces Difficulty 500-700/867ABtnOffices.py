n  = int(input())
s = input()

StoF = 0
FtoS = 0
current = s[0]
for i in range(1,n):
    if current != s[i]:
        if s[i] == 'F': 
            StoF += 1
            current = 'F'
        else: 
            FtoS += 1
            current = 'S'

if StoF > FtoS:
    print('YES')
else:
    print('NO')