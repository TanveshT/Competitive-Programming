t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    peopleServed = 0
    x = min(a, b, c)
    if x>= 1:
        peopleServed += 3 

    a, b, c = a-x, b-x, c-x

    x = min(a,b)
    peopleServed += min(1, x)

    a, b = a-x, b-x

    x = min(a,c)
    peopleServed += min(1, x)

    a, c = a-x, c-x

    x = min(b,c)
    peopleServed += min(1, x)

    b, c = b-x, c-x

    x = min(a,b,c)
    peopleServed += min(1,x)

    print(peopleServed)