import numpy as np
from numpy.linalg import norm

def sym_power_m(mat_A, x0, iter, tol):
    x = x0 / norm(x0, 2)
    y = np.dot(mat_A, x)
    mu = np.dot(x.T, y)
    k = 0
    while k < iter:
        # y = np.dot(mat_A, x)
        mu = np.dot(x.T, y)
        if norm(y, 2) == 0:
            break
        err = norm(x - (y/norm(y, 2)), 2)
        if err < tol:
            break
        x = y/norm(y, 2)
        y = np.dot(mat_A, x)

        k += 1

    return x, mu


if __name__ == "__main__":

    A = np.array([[4, -1, 1],
                  [-1, 3, -2],
                  [1, -2, 3]], dtype=np.float32)

    x = np.array([1, 0, 0], dtype=np.float32).reshape((3, 1))


    X, mu = sym_power_m(A, x, iter=9, tol=1e-4)
    print(X)
    print("\n")
    print(mu)







