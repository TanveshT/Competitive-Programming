k, r = map(int, input().split())
count = 0
while(True):
    count += 1
    if (((count*k)-r) % 10 == 0) or (count*k) %10 == 0 : break

print(count)