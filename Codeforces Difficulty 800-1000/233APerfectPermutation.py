n =  int(input())
a = [0] * n
if(n%2 == 0):
    for i in range(0,n,2):
        a[i] = i+2
        a[i+1] = i+1
    for i in range(n):
        print(a[i], end = " ")
else:
    print(-1)