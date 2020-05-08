w,x,y,z = list(map(int, input().split()))
if (w==x+y+z) or (x == w+y+z) or (y == w+x+z) or (z == w+y+x) or (x+y==w+z) or (x+z) == (y+w) or (x+w) == (y+z):
    print('YES')
else:
    print('NO')