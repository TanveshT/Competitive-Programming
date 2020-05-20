def solution1(start, length):

    prev = None
    for i in range(length,0, -1):
        for j in range(i):
            if prev == None:
                prev = start
            else:
                prev = prev^(start)

            start += 1
        start += (length - i)

    return prev

def getXOR(n):

    remainder = n%4

    if remainder == 0:
        return n
    elif remainder == 1:
        return 1
    elif remainder == 2:
        return n+1
    else:
        return 0

def solution(start, length):

    i = 0
    checkSum = None
    while(length > 0):
        left = start -1
        right = start + length -1

        x = getXOR(left) ^ getXOR(right)

        if checkSum == None:
            checkSum = x
        else:
            checkSum = checkSum^x

        length -= 1
        start = right + i + 1
        i += 1
    return checkSum

print(solution(0,3))
