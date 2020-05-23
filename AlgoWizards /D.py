t = int(input())

for _ in range(t):

    n, q = map(int, input().split())

    salary = 0

    for i in range(q):
        l, r, v = map(int, input().split())

        salary += ((r+1)-l)*v 

    print(salary)