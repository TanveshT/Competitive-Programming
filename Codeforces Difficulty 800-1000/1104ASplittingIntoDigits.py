n = int(input())
x = 0
y = 0
for i in range(9,0,-1):
    if n%i == 0:
        x = n//i
        y = i
        break

print(x)
print(' '.join(str(y)*x))