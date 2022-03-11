import random


def trans(arr):
    trans_mat = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr))]
    return trans_mat


def exp_v(ar, n):
    arr = trans(ar)
    p = 0.033
    m = 0
    for i in (arr[n]):
        m += i * p
    return m


def dis(ar, n):
    arr = trans(ar)
    p = 0.033
    mat = exp_v(arr, n)
    d = 0
    for i in (arr[n]):
        d += i**2 * p
    return d - mat**2


n = int(input())
m = [[random.randint(1, 30) for _ in range(n)] for _ in range(n)]
print(dis(m, 0))
