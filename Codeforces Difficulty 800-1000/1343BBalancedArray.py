t = int(input())

for _ in range(t):

    n = int(input())
    arr = [0] * n
    
    if n % 4 == 0:
        print('YES')
        l = 0; r = n//2
        for i in range(n):
            if (i+1)%2 == 0:
                arr[l] = i+1
                l+=1
            else:
                if i == (n-1): break
                arr[r] = i+1
                r += 1
        arr[n-1] = 3* (n//2) -1
        print(*arr, sep = " ")
    else:
        print('NO')