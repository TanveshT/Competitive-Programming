n = int(input())

x,y = 1,1
nextFib = x + y

answer = ''
for i in range(n):
    if (i+1) == x:
        answer += 'O'
    elif (i+1) == nextFib:
        answer += 'O'
        x = y
        y = nextFib
        nextFib = x+y
    else:
        answer += 'o'

print(answer)