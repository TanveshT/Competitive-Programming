t = int(input())
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v','w','x','y','z']
for _ in range(t):

    s = ''
    n, a, b = map(int, input().split())
    s += arr[0] * b
    #print(s)
    x = b-a
    i = 1
    for i in range(1,x+1):
        s += arr[i%26]
    

    res = s*(n//a) + s[:n%a]
    print(res)