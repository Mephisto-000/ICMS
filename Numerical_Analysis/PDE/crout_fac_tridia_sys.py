import numpy as np


def crout_fact_tridi(mat_A, mat_b):
    n = mat_A.shape[0]

    l_mat = np.zeros((n, n), dtype=np.float32)
    u_mat = np.zeros((n, n), dtype=np.float32)
    z_mat = np.zeros((n, 1), dtype=np.float32)
    x_mat = np.zeros((n, 1), dtype=np.float32)

    l_mat[0, 0] = mat_A[0, 0]
    u_mat[0, 1] = mat_A[0, 1] / l_mat[0, 0]
    z_mat[0, 0] = mat_b[0, 0] / l_mat[0, 0]

    for i in range(1, n-1):
        l_mat[i, i-1] = mat_A[i, i-1]
        l_mat[i, i] = mat_A[i, i] - l_mat[i, i-1]*u_mat[i-1, i]
        u_mat[i, i+1] = mat_A[i, i+1] / l_mat[i, i]
        z_mat[i, 0] = (mat_b[i, 0] - l_mat[i, i-1]*z_mat[i-1, 0]) / l_mat[i, i]

    l_mat[n-1, n-2] = mat_A[n-1, n-2]
    l_mat[n-1, n-1] = mat_A[n-1, n-1] - l_mat[n-1, n-2]*u_mat[n-2, n-1]
    z_mat[n-1, 0] = (mat_b[n-1, 0] - l_mat[n-1, n-2]*z_mat[n-2, 0]) / l_mat[n-1, n-1]

    x_mat[n-1, 0] = z_mat[n-1, 0]
    for i in range(n-2, -1, -1):
        x_mat[i, 0] = z_mat[i, 0] - u_mat[i, i+1]*x_mat[i+1, 0]

    return x_mat


# if __name__ == "__main__":
#
#     mat_A = np.array([[2, -1, 0, 0],
#                       [-1, 2, -1, 0],
#                       [0, -1, 2, -1],
#                       [0, 0, -1, 2]], dtype=np.float32)
#
#     mat_b = np.array([[1, 0, 0, 1]], dtype=np.float32).reshape((4, 1))
#
#     test = crout_fact_tridi(mat_A, mat_b)
#
#     print(test)

