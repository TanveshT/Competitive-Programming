n = int(input())
s = input().split('W')

count = 0
countArr = [] 
for x in s:
    if x == '': continue
    count += 1
    countArr.append(len(x))

print(count)
for x in countArr:
    print(x, end = " ")