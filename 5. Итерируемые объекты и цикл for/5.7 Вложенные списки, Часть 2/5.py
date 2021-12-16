n = int(input())

# Генерация пустой матрицы:
matrix = [[0] * n for i in range(n)]

# Счетчик чисел:
counter_1 = 1

# Счетчик для первой строки:
counter_2 = 0

# Центр матрицы:
matrix[n // 2][n // 2] = n ** 2

# Цикл матрицы:
for i in range(n // 2):

    # Верхняя горизонталь:
    for j in range(n - counter_2):
        matrix[i][j + i] = counter_1
        counter_1 += 1

    # Правая вертикаль:
    for j in range(i + 1, n - i):
        matrix[j][-i - 1] = counter_1
        counter_1 += 1

    # Нижняя горизонталь:
    for j in range(i + 1, n - i):
        matrix[-i - 1][-j - 1] = counter_1
        counter_1 += 1

    # Левая вертикаль:
    for j in range(i + 1, n - (i + 1)):
        matrix[-j - 1][i] = counter_1
        counter_1 += 1

    counter_2 += 2

# Вывод матрицы:
for string in range(n):
    print(*matrix[string])
