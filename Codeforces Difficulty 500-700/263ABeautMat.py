rowContainingOne, columnContainingOne = 0, 0

for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            columnContainingOne = j + 1
            rowContainingOne = i + 1

print(abs(3-rowContainingOne) + abs(3-columnContainingOne))