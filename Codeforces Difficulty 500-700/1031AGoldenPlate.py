w, h, k = map(int, input().split())

count = 0

for i in range(k):
    count += ((w*h) - ((w-2)*(h-2)))
    w -= 4
    h -= 4

print(count)