n = int(input())

b = list(map(int, input().split()))

prevPos = 0
for i in range(n):
    
    if b[i] + prevPos <= 0:
        b[i] = 0
    else:
        b[i] += prevPos
        if b[i] > prevPos:
            prevPos = b[i]
    
       
print(*b, sep = " ")