n = int(input())

count = 1
previous = None
for i in range(n):
    x = int(input())
    if previous == None:
        previous = x
    else:
        if previous!=x:
            count += 1
            previous = x

print(count)