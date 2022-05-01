import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la



class Star:
    def __init__(self, name, init_pos, init_vel, mass):
        self.name = name
        self.p = init_pos
        self.v = init_vel
        self.m = mass


class Simulation:
    def __init__(self, stars, t, dt):
        self.g_const = 6.672e-11  # Nm^2 / kg^2

        self.names = np.array([s.name for s in stars], dtype=str)
        self.pos = np.array([s.p for s in stars], dtype=np.float64)
        self.vel = np.array([s.v for s in stars], dtype=np.float64)
        self.mass = np.array([s.m for s in stars], dtype=np.float64)

        self.time_length = t
        self.time_step = dt
        self.time_range = int(np.floor(t / dt))

        self.result_pos = []
        self.result_vel = []


def rk4(pos_0, vel_0, M_1, M_2, t_l, dt, G):
    mu = G*(M_1 + M_2)
    pos_list = [pos_0]
    vel_list = [vel_0]

    t_tmp = 0
    while t_tmp <= t_l:
        r_3 = la.norm(pos_list[-1])**3

        v1 = vel_list[-1]
        a1 = -mu * pos_list[-1] / r_3

        v2 = v1 + dt*0.5*v1
        a2 = a1 + dt*0.5*a1

        v3 = v1 + dt*0.5*v2
        a3 = a1 + dt*0.5*a2

        v4 = v1 + dt*v3
        a4 = a1 + dt*a3

        tmp_next_pos = pos_list[-1] + dt*(v1 + 2*v2 + 2*v3 + v4) / 6
        tmp_next_vel = vel_list[-1] + dt * (a1 + 2 * a2 + 2 * a3 + a4) / 6

        pos_list.append(tmp_next_pos)
        vel_list.append(tmp_next_vel)

        t_tmp += dt

    return pos_list, vel_list


if __name__ == "__main__":
    # sec_in_day = 24 * 3600.0
    # t = 365.0 * sec_in_day
    # dt = 10.0 * sec_in_day

    G = 6.67
    M1_mass = 100
    M2_mass = 2
    R = 10


    # t_length = 5000
    # dt = 0.01

    M2_v_0 = np.sqrt(G*M1_mass / R)


    M_1 = Star("M1", np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), M1_mass)
    M_2 = Star("M2", np.array([R, 0.0, 0.0]), np.array([0.0, M2_v_0, 0.0]), M2_mass)



    t_length = (5/2)*np.pi

    dt = t_length / 1000

    r_vec = M_2.p - M_1.p
    v_vec = M_2.v - M_1.v

    test_pos, test_vel = rk4(r_vec, v_vec, M_1.m, M_2.m, t_length, dt, G)

    plt.style.use('ggplot')
    for i in test_pos:
        plt.plot(i[0], i[1], "r.")

    plt.plot(0.0, 0.0, "b.")
    plt.axis("equal")
    plt.show()

    print(len(test_pos))






