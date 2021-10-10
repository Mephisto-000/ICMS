import os
import numpy as np
import matplotlib.pyplot as plt



def func_u(x):
    out = np.sin(np.power(x, 0.2))
    return out




if __name__ == "__main__":

    main_path = os.getcwd()
    u_path = os.path.join(main_path, "u.csv")

    test = np.genfromtxt(u_path, delimiter=',')
    print(test.shape, "\n")
    data = test[1::][0::]
    title = test[0][0::]

    t, x, y, u = [], [], [], []
    for i in range(1, 1501):
        tmp_x = data[i][1]
        tmp_y = data[i][2]
        tmp_t = data[i][0]
        tmp_u = data[i][3]

        x.append(tmp_x)
        y.append(tmp_y)
        t.append(tmp_t)

        u.append(tmp_u)


    time = np.linspace(1, 150, 150)
    fu = func_u(time)

    plt.plot(time, fu, "b")
    plt.title("u(t)", fontsize=25)
    # plt.show()



    plt.plot(t, u, "ro")
    plt.show()

