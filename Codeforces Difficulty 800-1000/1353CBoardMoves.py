t = int(input())

for _ in range(t):
    
    n = int(input())
    validLayers = n//2
    count = 0
    for i in range(1,validLayers+1):
        count += 8*i*i
    print(count) 