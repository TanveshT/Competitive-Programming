s = input()
count = 0
for x in s:
    if x.isnumeric():
        x = int(x)
        if x%2!=0:
            count += 1
    else:
        if x in ['a', 'e', 'i', 'o', 'u']:
            count+=1

print(count)