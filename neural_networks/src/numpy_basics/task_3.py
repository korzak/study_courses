# coding=utf-8

import numpy as np

# Задача: перемножьте две матрицы!
#
# На вход программе подаются две матрицы, каждая в следующем формате: на первой
# строке два целых положительных числа n и m, разделенных пробелом - размерность матрицы. В следующей строке
# находится n⋅m целых чисел, разделенных пробелами - элементы матрицы. Подразумевается, что матрица заполняется
# построчно, то есть первые m чисел - первый ряд матрицы, числа от m+1 до 2⋅m - второй, и т.д.
#
# Напечатайте произведение матриц XYT, если они имеют подходящую форму, или строку "matrix shapes do not match",
# если формы матриц не совпадают должным образом.

# Test data to skip input
# matrix_x = np.array([[8, 7, 7], [14, 4, 6]])
# matrix_y = np.array([[5, 5, 1], [5, 2, 6], [3, 3, 9], [1, 4, 6]])

x_shape = tuple(map(int, raw_input().split()))
matrix_x = np.fromiter(map(int, raw_input().split()), np.int).reshape(x_shape)

y_shape = tuple(map(int, raw_input().split()))
matrix_y = np.fromiter(map(int, raw_input().split()), np.int).reshape(y_shape)

try:
    print(matrix_x.dot(matrix_y.T))
except ValueError:
    print('matrix shapes do not match')
