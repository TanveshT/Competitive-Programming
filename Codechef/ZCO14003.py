try:
    t = int(input())
    arr = []

    for i in range(t):
        arr.append(int(input()))

    arr = sorted(arr)

    x = 0

    for i in range(t):
        x = max(x, arr[i] * (t-i))

    print(x)
    
except Exception:
    pass