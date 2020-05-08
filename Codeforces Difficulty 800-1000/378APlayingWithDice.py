a, b = map(int, input().split())
awin, draw, bwin = 0,0,0
for i in range(1, 7):
    if abs(a-i) < abs(b-i): awin +=1
    elif abs(a-i) == abs(b-i): draw += 1
    else: bwin += 1

print(awin, draw, bwin)