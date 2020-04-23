s = input()
n = len(s)

a = [[0,0]] * n
qcount = 0
for i in range(n):
    if s[i] == 'Q':
        qcount += 1
    a[i][0] = int(qcount)

qcount = 0
for i in range(n-1,-1,-1):
    if s[i] == 'Q': 
        qcount += 1
    a[i][1] = int(qcount)

count = 0
print(a)
for i in range(n):
    if s[i] == 'A':
        count += min(a[i])
print(count)