# 1. Квадратная матрица, симметричная относительно главной диагонали, задана верхним треугольником в виде одномерного массива. Восстановить исходную матрицу и напечатать по строкам. 

def restore_matrix(triangle):
    n = int((2 * len(triangle) + 0.25) ** 0.5 - 0.5)
    matrix = [[0] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = matrix[j][i] = triangle[index]
            index += 1
    for row in matrix:
        print(row)

    return matrix

# Проверка
triangle = [2, 9, 2, 5, 4, 6]
matrix = restore_matrix(triangle)