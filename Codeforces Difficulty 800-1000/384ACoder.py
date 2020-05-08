n = int(input())
oddFlag = (n%2!=0)
half = n//2
if oddFlag:print((((n+1)//2) ** 2) + (((n-1)//2) ** 2))
else: print(n//2*n)
for i in range(n):
    if (i+1) % 2 != 0:
        print('C.'*half, end = "")
        if oddFlag: print('C',end = "")
    else:
        print('.C'*half,end = "")
        if oddFlag: print('.',end = "")

    print()