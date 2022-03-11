from sem2.лаб2 import modmatrix
import numpy as np

m = modmatrix.matrix()
# 1 - возведение в квадрат
# m.sqr_matrix()
# np.linalg.matrix_power(m.matrix, 2)
# 2 - транспорнирование
# m.trans()
# np.array(m.matrix).transpose()
# 3 - определитель матрицы
print(np.linalg.det(m.matrix))
print(m.op_matrix())
