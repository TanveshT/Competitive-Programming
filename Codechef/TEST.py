a = []

x = int(input())
a.append(x)

while( x!=42):
    x = int(input())
    a.append(x)

for i in a:
    if i!= 42:
        print(i)