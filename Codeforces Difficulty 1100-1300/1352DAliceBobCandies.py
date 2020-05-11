t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    alice = a.pop(0)
    bob = 0
    n -= 1

    move = 1

    previous = alice

    flag = False
    while(n > 0):
        current = 0
        if move%2 != 0:
            while(current <= previous):
                if n == 0:
                    break
                current += a.pop()
                n -= 1
            bob += current
        else:
            while(current <= previous):
                if n == 0:
                    break
                current += a.pop(0)
                n -= 1
            alice += current
        previous = current
        move += 1


    if flag:
        move -= 1
        if move%2!=0:
            bob-=previous
        else:
            alice-=previous

    print(move, alice, bob)