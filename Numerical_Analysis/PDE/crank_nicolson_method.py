import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm, inv
from crout_fac_tridia_sys import crout_fact_tridi


def init_func(x):
    return np.sin((np.pi/2)*x)


def tridiag_mat(lbda, n, flag="A"):
    mat = np.zeros((n, n), dtype=np.float32)
    if flag == "B":
        lbda = -lbda
    for i in range(n):
        for j in range(n):
            index_i = i + 1
            index_j = j + 1
            if index_j == index_i:
                mat[i, j] = 1 + lbda
            elif (index_j == index_i + 1) or (index_j == index_i - 1):
                mat[i, j] = -(lbda/2)
            else:
                mat[i, j] = 0

    return mat


def c_n_m(end_pt, max_time, alpha, m, N):
    w = np.zeros((m, N), dtype=np.float32)

    h = end_pt/m
    k = max_time/N
    lbda = ((alpha**2)*k)/(h**2)
    w[m-1, :] = 0

    for i in range(0, m-1):
        w[i, 0] = init_func((i+1)*h)

    mat_A = tridiag_mat(lbda, m)
    mat_B = tridiag_mat(lbda, m, flag="B")

    for j in range(N-1):
        mat_b = np.dot(mat_B, w[:, j]).reshape((m, 1))
        w_j_next = crout_fact_tridi(mat_A, mat_b)
        w[:, j+1] = w_j_next.flatten()

    return w


def exact_f(x, t):
    return np.exp(-t*((np.pi**2)/4))*np.sin((np.pi/2)*x)


if __name__ == "__main__":
    w = c_n_m(2, 1, 1, m=10, N=10000)

    nu = w[:, 5000]
    print(nu)

    x_i = np.linspace(0, 2, 10)
    y_exact = exact_f(x_i, 0.5)

    # print(nu.T)

    plt.style.use("ggplot")
    plt.plot(x_i, y_exact, "-", label="true")
    plt.plot(x_i, nu, "--", label="nu")
    plt.plot(x_i, nu-y_exact, "--")
    plt.legend()
    plt.show()



