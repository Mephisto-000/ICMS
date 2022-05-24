import numpy as np
from numpy.linalg import norm


def cg_m(mat_A, mat_b, iter, tol, pre_mat=None, x0=None):
    m, n = mat_A.shape
    b_dim = mat_b.shape
    if x0 is None:
        x0 = np.zeros(b_dim, dtype=np.float32)
    if pre_mat is None:
        pre_mat = np.eye(m, n, dtype=np.float32)
    x = x0.copy()
    r = mat_b - np.dot(mat_A, x)
    w = np.dot(pre_mat, r)
    v = np.dot(pre_mat.T, w)
    alpha = np.sum(w**2)
    k = 0
    while k < iter:
        v_flag = norm(v, np.inf)
        if v_flag < tol:
            break

        u = np.dot(mat_A, v)
        t = alpha / np.dot(u.T, v)
        x = x + t*v
        r = r - t*u
        w = np.dot(pre_mat, r)
        beta = np.sum(w**2)
        if beta < tol:
            if norm(r, np.inf) < tol:
                break
        s = beta/alpha
        v = np.dot(pre_mat, w) + s*v
        alpha = beta
        k += 1

    return x, r, k


if __name__ == "__main__":
    mat_A = np.array([[4, 3, 0],
                      [3, 4, -1],
                      [0, -1, 4]], dtype=np.float32)

    mat_b = np.array([[24, 30, -24]], dtype=np.float32).T

    x, r, k = cg_m(mat_A, mat_b, 2, 1e-8)

    print(x)
    print(r)
    print(k)

