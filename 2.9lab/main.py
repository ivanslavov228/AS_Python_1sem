import numpy as np

# Загрузка матриц из файлов
with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
    data1 = f1.read().strip().split('\n\n')
    data2 = f2.read().strip().split('\n\n')

matrices1 = []
matrices2 = []

# Преобразование строк в матрицы для первого файла
for block in data1:
    rows = block.strip().split('\n')
    matrix = [list(map(int, row.split())) for row in rows]
    matrices1.append(matrix)

# Преобразование строк в матрицы для второго файла
for block in data2:
    rows = block.strip().split('\n')
    matrix = [list(map(int, row.split())) for row in rows]
    matrices2.append(matrix)

# Меняем местами нечётные по порядку матрицы (индексы 0, 2, 4, ...)
min_len = min(len(matrices1), len(matrices2))
for i in range(0, min_len, 2):  # только четные индексы соответствуют нечетным порядковым номерам
    matrices1[i], matrices2[i] = matrices2[i], matrices1[i]

# Запись обратно в файлы
with open('file1.txt', 'w') as f1, open('file2.txt', 'w') as f2:
    for matrix in matrices1:
        for row in matrix:
            f1.write(' '.join(map(str, row)) + '\n')
        f1.write('\n')
    for matrix in matrices2:
        for row in matrix:
            f2.write(' '.join(map(str, row)) + '\n')
        f2.write('\n')

# Вывод содержимого файлов
print("Содержимое первого файла:")
with open('file1.txt', 'r') as f1:
    print(f1.read())

print("Содержимое второго файла:")
with open('file2.txt', 'r') as f2:
    print(f2.read())
