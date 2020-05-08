a = input()
instructions = input()

l = 1
for x in instructions:
    if a[l-1] == x:
        l += 1

print(l)