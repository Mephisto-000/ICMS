import os
import numpy as np
import matplotlib.pyplot as plt



def plot_result(path):
    t = np.loadtxt(path, delimiter=",")
    r1x, r1y, r2x, r2y = [], [], [], []
    v1x, v1y, v2x, v2y = [], [], [], []

    for i in t:
        r1x.append(i[0])
        r1y.append(i[1])
        r2x.append(i[2])
        r2y.append(i[3])

        v1x.append(i[4])
        v1y.append(i[5])
        v2x.append(i[6])
        v2y.append(i[7])

    for i, j, m, n in zip(r1x, r1y, r2x, r2y):
        print(i, j, m, n)

    plt.style.use('ggplot')
    plt.plot(0.0, 0.0, color="black", marker="o", markersize=20)
    plt.plot(r1x, r1y, "r.", label="r1(t)")
    plt.plot(r2x, r2y, "b.", label="r2(t)")
    plt.title("r1(t), r2(t), M1 = 1, M2 = 1, e = 0.5", fontsize=20)
    plt.axis("equal")
    plt.legend(fontsize=15)
    plt.show()




    x1_len = [i for i in range(len(r1x))]
    y1_len = [i for i in range(len(r1y))]

    plt.plot(x1_len, r1x, "r-o", label="rx")
    plt.plot(y1_len, r1y, "b-o", label="ry")
    plt.title("r1(t), x and y positions", fontsize=20)
    plt.legend(fontsize=15)
    plt.show()


    x2_len = [i for i in range(len(r2x))]
    y2_len = [i for i in range(len(r2y))]

    plt.plot(x2_len, r2x, "r-o", label="rx")
    plt.plot(y2_len, r2y, "b-o", label="ry")
    plt.title("r2(t), x and y positions", fontsize=20)
    plt.legend(fontsize=15)
    plt.show()



if __name__ == "__main__":
    main_path = os.getcwd()
    result_path = main_path + os.sep + "result.txt"
    plot_result(result_path)


