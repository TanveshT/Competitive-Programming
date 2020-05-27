try:
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        x = arr[0]

        count = 0
        for i in arr:
            if i <= x:
                count += 1
            x = min(i, x)
        

        print(count)
except Exception:
    pass