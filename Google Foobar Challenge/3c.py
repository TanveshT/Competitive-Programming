def solution(x, y):

    x, y = int(x), int(y)
    count = 0
    if max(x,y) % min(x,y) == 0 and x != 1 and y != 1:
        return "impossible"

    while not (x==1 or y == 1):
        if x > y:
            count += x//y
            x, y = x%y, y
        else:
            count += y//x
            x, y = x, y%x
  
    return count + max(x,y) - 1

print(solution('2','1'))