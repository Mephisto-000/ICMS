import numpy as np


def gauss_seidel_m(mat_A, mat_b, iter_n, tol, x0=None):
    m, n = mat_A.shape
    b_dim = mat_b.shape

    if x0 is None:
        x0 = np.zeros(b_dim, dtype=np.float32)
    x = x0.copy()
    k = 0
    while k < iter_n:
        XO = x.copy()
        for i in range(m):
            upper_mat = np.dot(mat_A[i, i+1:], XO[i+1:])
            lower_mat = np.dot(mat_A[i, :i], x[:i])
            x[i] = (1/mat_A[i][i])*(-(upper_mat + lower_mat) + mat_b[i])

        err = np.linalg.norm(XO - x, np.inf) / np.linalg.norm(x, np.inf)
        if err < tol:
            break
        k += 1

    return x, k





if __name__ == "__main__":
    mat_A = np.array([[10, -1, 2, 0],
                      [-1, 11, -1, 3],
                      [2, -1, 10, -1],
                      [0, 3, -1, 8]], dtype=np.float32)

    mat_b = np.array([[6, 25, -11, 15]], dtype=np.float32).T




    x, k = gauss_seidel_m(mat_A, mat_b, 2, 1e-3)

    print(x)
    print(k)

