rowFib = [1, 2]

while rowFib[-1] < 4000000:
    longRow = len(rowFib)
    rowFib.append(rowFib[longRow-2]+rowFib[longRow-1])

evenList = list(range(2, len(rowFib), 2))

for item in evenList:
    print(rowFib[item])
