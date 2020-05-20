def solution(x, y):
    add = 1
    num = 0
    for i in range(x):
        num+=add
        add+=1
    add = x
    for i in range(y-1):
        num+=add
        add+= 1
    return num

x,y = map(int,input().split())

print(solution(x,y))
