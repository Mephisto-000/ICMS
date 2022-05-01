import numpy as np
import matplotlib.pyplot as plt


def jacobi_m(mat_A, mat_b, iter_n, tol):
    k = 0
    n = mat_A.shape[0]
    x0 = np.zeros(n).reshape((n, 1))
    while k <= iter_n:
        XO = np.zeros(n).reshape((n, 1))
        for i in range(n):
            md_left = mat_A[i, :i]@x0[:i]
            md_right = mat_A[i, i+1:]@x0[i+1:]
            XO[i] = (1/mat_A[i][i])*(-(md_left + md_right) + mat_b[i])

        err = np.linalg.norm(XO - x0, np.inf) / np.linalg.norm(XO, np.inf)
        if err < tol:
            break
        x0 = XO
        k += 1

    return x0, k


# if __name__ == "__main__":
#     test_sys_A = np.array([[10, -1, 2, 0],
#                          [-1, 11, -1, 3],
#                          [2, -1, 10, -1],
#                          [0, 3, -1, 8]], dtype=np.float16)
#
#     test_sys_b = np.array([[6, 25, -11, 15]], dtype=np.float16).T
#
#     print(test_sys_A.shape)
#     print(test_sys_b.shape)
#
#     x, k = jacobi_m(test_sys_A, test_sys_b, 10, 1e-2)
#
#     print(x)
#     print(k)

