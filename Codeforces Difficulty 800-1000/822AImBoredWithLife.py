a, b = map(int, input().split())
x = min(a,b)
fact = 1
for i in range(1,x+1):
    fact *= i
print(fact)