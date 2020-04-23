n, k = map(int, input().split())
time = 4 * 60

count = 0
currentTime = k
for i in range(n):
    currentTime += (5*(i+1))
    if currentTime > time: break
    count += 1 

print(count)