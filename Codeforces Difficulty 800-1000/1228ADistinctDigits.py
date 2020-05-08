l,r = map(int,input().split())
for i in range(l,r+1):
    a=str(i)
    b=set(a)
    if(len(a)==len(b)):
        res=a
        break
    else:
        res=-1

print(res)