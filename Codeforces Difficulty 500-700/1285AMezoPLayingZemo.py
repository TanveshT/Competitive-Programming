n = int(input())
s = input()

l, r = 0, 0
for x in s:
    if x == 'L': l += 1
    else: r += 1
    

print(l + r + 1)
