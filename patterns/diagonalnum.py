
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print("")