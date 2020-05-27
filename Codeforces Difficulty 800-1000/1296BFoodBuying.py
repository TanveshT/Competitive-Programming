t = int(input())

for _ in range(t):
    s = int(input())
    spent = 0
    while(s > 1):
        spent += (s//10)*10
        cashback = s//10
        s -= ((s//10)*10 - s//10)

    print(spent+s)