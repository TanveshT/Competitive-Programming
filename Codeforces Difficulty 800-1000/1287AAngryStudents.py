t = int(input())

for _ in range(t):
    
    n = int(input())
    s = input()

    maxDistance = 0
    current = None
    for i in range(n):
        if s[i] == 'A':
            current = 0
        elif current != None:
            current += 1
            maxDistance = max(current, maxDistance)

    print(maxDistance)