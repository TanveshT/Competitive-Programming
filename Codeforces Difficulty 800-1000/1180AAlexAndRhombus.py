n = int(input())

an = ((n-1)*2) + 1   # Arithmetic Progression for number of cells in middle
count = 0
for i in range(an,0,-2):
    count += i
print((count-an)*2 + an)