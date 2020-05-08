n = int(input())
perimeter = 10000003
for i in range(1,n+1):
    if n%i == 0:
        checkPerimeter = 2*i + 2*(n//i)
        if checkPerimeter <= perimeter:
            perimeter = checkPerimeter
print(perimeter)