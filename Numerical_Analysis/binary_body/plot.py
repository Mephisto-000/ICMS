import os
import numpy as np
import matplotlib.pyplot as plt



def plot_result(path):
    t = np.loadtxt(path, delimiter=",")
    rx, ry = [], []
    vx, vy = [], []

    for i in t:
        rx.append(i[1])
        ry.append(i[2])
        vx.append(i[3])
        vy.append(i[4])

    for i, j, m, n in zip(rx, ry, vx, vy):
        print(i, j, m, n)

    plt.style.use('ggplot')
    plt.plot(rx, ry, "r.")
    plt.title("r(t)", fontsize=20)
    plt.axis("equal")
    plt.show()

    x_len = [i for i in range(len(rx))]
    y_len = [i for i in range(len(ry))]

    plt.plot(x_len, rx, "r-o", label="rx")
    plt.plot(y_len, ry, "b-o", label="ry")
    plt.title("r(t), x-position", fontsize=20)
    plt.legend(fontsize=15)
    plt.show()



# if __name__ == "__main__":
#     main_path = os.getcwd()
#     result_path = main_path + os.sep + "result.txt"
#     plot_result(result_path)
