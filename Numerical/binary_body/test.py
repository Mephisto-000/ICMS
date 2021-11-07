import numpy as np
from numpy import linalg as la



if __name__ == "__main__":
    # t1 = np.array([2, 2, 2])
    # t2 = np.array([0, 0, 0])

    t1 = np.array([1, 1])
    t2 = np.array([0, 0])

    r_vector = t1 - t2
    test = la.norm(r_vector)
    print(test)
    print("\n")

    test2 = np.arctan(r_vector[1]/r_vector[0])
    print(test2)


