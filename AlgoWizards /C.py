t = int(input())

for _ in range(t):

    n = int(input())
    s = input()

    zeroCount = 0
    oneCount = 0

    x = [0] * n
    for i in range(n):
        if s[i] == '0':
            x[i] = oneCount
            zeroCount += 1
        else:
            x[i] = zeroCount
            oneCount += 1

    count = 0
    for i in x:
        count += i
    
    print(count)