s = input()

h, e, iFirst, d, iSecond = False, False, False, False, False

for x in s:
    if x == 'h' and not h:
        h = True
    if x == 'e' and h and not e:
        e = True
    if x == 'i' and e and not iFirst:
        iFirst = True
    if x == 'd' and iFirst:
        d = True
    if x == 'i' and d:
        iSecond = True


if h and e and d and iFirst and iSecond:
    print('YES')
else:
    print('NO')
