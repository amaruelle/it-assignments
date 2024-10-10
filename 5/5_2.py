# 2. Для заданной квадратной матрицы сформировать одномерный массив из ее диагональных элементов. Найти след матрицы, просуммировав элементы одномерного массива. Преобразовать исходную матрицу по правилу: четные строки разделить на полученное значение, нечетные оставить без изменения. 

def diagonal_elements(matrix):
    n = len(matrix)
    diagonal = [matrix[i][i] for i in range(n)]
    trace = sum(diagonal)
    for i in range(n):
        for j in range(n):
            if i % 2 == 1:
                matrix[i][j] = round(matrix[i][j] / trace, 1)
    for row in matrix:
        print(row)
    print("След матрицы:", trace)

# Проверка
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_elements(matrix)