s = input()
n = len(s)
countA = s.count('a')
if countA > n/2:
    print(n)
else:
    print(countA*2 - 1)