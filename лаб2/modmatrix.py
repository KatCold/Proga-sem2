import copy


class matrix(list):
    def __init__(self):
        super().__init__()
        a = int(input())
        self.matrix = [list(map(int, input().split())) for _ in range(a)]

    def sqr_matrix(self):
        mat = self.matrix
        double_mat = []
        for i in range(len(mat)):
            double_mat.append([])
            for j in range(len(mat)):
                double_mat[i].append(0)
                for k in range(len(mat)):
                    double_mat[i][j] += mat[i][k] * mat[k][j]
        return double_mat

    def trans(self):
        trans_mat = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix))]
        return trans_mat

    # def minor(self, arr, i, j):
    #     min_arr = copy.deepcopy(arr)
    #     min_arr.pop(i)
    #     for k in range(len(min_arr)):
    #         min_arr[k].pop(j)
    #     return (-1)**i * self.op_matrix(min_arr)
    #
    # def op_matrix(self, m=None):
    #     if m is None:
    #         m = self.matrix
    #     mat = copy.deepcopy(m)
    #     if len(m) == 1:
    #         return m[0][0]
    #     op = 0
    #     for i in range(len(m)):
    #         op += mat[i][0] * self.minor(m, i, 0)
    #     return op

    def minor(self, arr, i, j):
        min_arr = copy.deepcopy(arr)
        min_arr.pop(i)
        for k in range(len(min_arr)):
            min_arr[k].pop(j)
        return min_arr

    def op_matrix(self, m=None):
        if m is None:
            m = self.matrix
        mat = copy.deepcopy(m)
        if len(m) == 1:
            return m[0][0]
        op = 0
        for i in range(len(m)):
            op += mat[i][0] * self.op_matrix(self.minor(m, i, 0)) * (-1)**i
        return op

