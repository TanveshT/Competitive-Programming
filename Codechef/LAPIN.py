try:
    t = int(input())
    for _ in range(t):
        s = input()
        x = [0] * 26
        y = [0] * 26
        n = len(s)
        half = n//2
        if n%2==0:
            for i in range(half):
                x[ord(s[i]) - 97] += 1
                y[ord(s[i+half]) - 97] += 1
        else:
            for i in range(half):
                x[ord(s[i]) - 97] += 1
                y[ord(s[i+half+1]) - 97] += 1

            
        flag = True
        for i in range(26):
            if x[i] != y[i]:
                flag = False
                break
        
        if flag:
            print('YES')
        else:
            print('NO')

except Exception:
    pass