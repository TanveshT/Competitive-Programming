n = int(input())
count = 0
while(n!=0):
    if n%10 == 4 or n%10 == 7:
        count += 1
    n //= 10

count = str(count)
flag = True
for x in count:
    if x != '4' and x != '7':
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')