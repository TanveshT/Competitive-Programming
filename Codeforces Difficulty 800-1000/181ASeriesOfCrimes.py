n, m = map(int, input().split())

rowSet = [0] * 101
columnSet = [0] * 101
for i in range(n):
    row = input()
    for j in range(m):
        if row[j] == '*':
            rowSet[i+1] += 1
            columnSet[j+1] += 1

rowIndex, columnIndex = None, None
for i in range(1,101):
    if rowSet[i] == 1:
        rowIndex = i
    if columnSet[i] == 1:
        columnIndex = i

print(rowIndex, columnIndex, sep = " ")
