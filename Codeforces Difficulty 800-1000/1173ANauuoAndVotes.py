x, y, z = map(int, input().split())

res = ''
if x > y and x > (y + z):
    res += '+'
elif y > x and y > (x + z):
    res += '-'
elif x == y and z == 0:
    res += '0'
else:
    res += '?'

print(res)