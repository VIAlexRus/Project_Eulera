#Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

rowFib = [1, 2]

while rowFib[-1] < 4000000:
    longRow = len(rowFib)
    rowFib.append(rowFib[longRow-2]+rowFib[longRow-1])

evenList = list(range(2, len(rowFib), 2))

for item in evenList:
    print(rowFib[item])
