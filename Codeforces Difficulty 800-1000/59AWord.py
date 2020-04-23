s = input()

countUpper = 0
countLower = 0
for x in s:
    if x.isupper(): countUpper+=1
    else: countLower += 1

if countUpper > countLower:
    print(s.upper())
else:
    print(s.lower())

    