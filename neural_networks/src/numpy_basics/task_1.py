# coding=utf-8

import numpy as np

# Создайте и напечатайте (с помощью функции print) массив класса np.ndarray ширины 4 и высоты 3 с двойками на главной
# диагонали и единицами на первой диагонали над главной
print(2 * np.eye(3, 4, 0) + np.eye(3, 4, 1))
