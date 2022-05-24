import numpy as np


def sor_method(mat_A, mat_b, omega, iter_n, tol, x0=None):
    m, n = mat_A.shape
    b_dim = mat_b.shape

    if x0 is None:
        x0 = np.ones(b_dim, dtype=np.float32)
    x = x0.copy()
    k = 0
    while k < iter_n:
        XO = x.copy()
        for i in range(m):
            upper_mat = np.dot(mat_A[i, i+1:], XO[i+1:])
            lower_mat = np.dot(mat_A[i, :i], x[:i])
            x[i] =(1 - omega)*XO[i] + (1/mat_A[i][i])*(omega*(-(upper_mat + lower_mat) + mat_b[i]))

        err = np.linalg.norm(XO - x, np.inf) / np.linalg.norm(x, np.inf)
        if err < tol:
            break
        k += 1

    return x, k


if __name__ == "__main__":
    mat_A = np.array([[4, 3, 0],
                      [3, 4, -1],
                      [0, -1, 4]], dtype=np.float32)

    mat_b = np.array([[24, 30, -24]]).T

    x, k = sor_method(mat_A, mat_b, 1.25, 3, 1e-6)

    print(x)
    print(k)




