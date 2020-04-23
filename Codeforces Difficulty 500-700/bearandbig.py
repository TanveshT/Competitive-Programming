l, b = map(int, input().split())

count = 0
while(True):
    l *= 3
    b *= 2
    count += 1
    if l > b: break

print(count)