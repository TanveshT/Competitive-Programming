n = int(input())

X,Y,Z = 0,0,0
for _ in range(n):
    x, y, z = map(int, input().split())
    X += x; Y+=y; Z+=z
    
if X==Y==Z==0:
    print('YES')
else:
    print('NO')