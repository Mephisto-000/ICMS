import numpy as np
from numpy.linalg import norm


def power_m(mat_A, x0, iter, tol):
    x_p_abs = norm(x0, np.inf)
    xp_list = np.where(np.abs(x0) == x_p_abs)
    p_index = np.min(xp_list[0])
    xp = x0[p_index]
    x = x0 / xp
    y = np.dot(mat_A, x)
    mu = y[p_index]
    k = 0
    while k < iter:
        yp = y[p_index]
        mu = yp
        if yp == 0:
            break
        err = norm(x - (y/yp), np.inf)
        if err < tol:
            break
        x = y / yp
        y = np.dot(mat_A, x)
        y_p_abs = norm(y, np.inf)
        yp_list = np.where(np.abs(y) == y_p_abs)
        p_index = min(yp_list[0])

        k += 1

    return x, mu


if __name__ == "__main__":

    A = np.array([[-4, 14, 0],
                  [-5, 13, 0],
                  [-1, 0, 2]], dtype=np.float32)

    x = np.array([1, 1, 1], dtype=np.float32).reshape((3, 1))

    X, mu = power_m(A, x, iter=6, tol=1e-4)
    print(X)
    print("\n")
    print(mu)

