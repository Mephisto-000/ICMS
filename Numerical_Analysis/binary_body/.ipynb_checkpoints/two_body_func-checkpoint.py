import numpy as np
import matplotlib.pyplot as plt
from math import floor

np.seterr(divide='ignore', invalid='ignore')


class Star:
    def __init__(self, name, init_pos, init_vel, mass):
        self.name = name
        self.p = init_pos
        self.v = init_vel
        self.m = mass


class Simulation:
    def __init__(self, stars, t, dt):
        self.g_constant = 6.672e-11  # Nm^2 / kg^2

        self.mass = np.array([[s.m] for s in stars], dtype=np.float64)  # shape : (n, 1, 1)
        self.vel = np.array([s.v for s in stars], dtype=np.float64)     # shape : (n, 1, 3)
        self.pos = np.array([s.p for s in stars], dtype=np.float64)     # shape : (n, 1, 3)
        self.names = np.array([s.name for s in stars], dtype=str)

        self.cen_p = np.sum(np.multiply(self.mass, self.pos), axis=0) / np.sum(self.mass, axis=0)
        self.cen_v = np.sum(np.multiply(self.mass, self.vel), axis=0) / np.sum(self.mass, axis=0)

        self.shift_pos = np.zeros(shape=self.pos.shape)
        self.shift_vel = np.zeros(shape=self.vel.shape)

        self.time_length = t
        self.time_step = dt
        self.time_range = floor(t/dt)

        self.result_pos = []
        self.result_vel = []


    def shift_pos_vel(self):
        tmp_pos = self.pos
        tmp_vel = self.vel

        for p in tmp_pos: p -= self.cen_p
        for v in tmp_vel: v -= self.cen_v

        self.shift_pos = tmp_pos
        self.shift_vel = tmp_vel

    def acceleration(self, pos):
        tmp_mass = self.mass
        d_vector = np.nan_to_num(pos[None, :] - pos[:, None])
        r_3 = np.nan_to_num(np.sum(np.abs(d_vector) ** 2, axis=-1)**1.5).reshape((pos.shape[0], pos.shape[0], 1))
        return self.g_constant * np.sum((np.nan_to_num(np.divide(d_vector, r_3)) * np.tile(tmp_mass, (pos.shape[0], 1)).reshape(pos.shape[0], pos.shape[0], 1)), axis=1)


    def rk4(self, pos, vel, dt):
        v1 = vel
        a1 = self.acceleration(pos)

        v2 = vel + a1*0.5*dt
        a2 = self.acceleration(pos + v1*0.5*dt)

        v3 = vel + a2*0.5*dt
        a3 = self.acceleration(pos + v2*0.5*dt)

        v4 = vel + a3*dt
        a4 = self.acceleration(pos + v3*dt)

        return pos + ((v1 + 2*v2 + 2*v3 + v4)/6)*dt, vel + ((a1 + 2*a2 + 2*a3 + a4)/6)*dt


    def result_data(self):
        tmp_pos = self.shift_pos
        tmp_vel = self.shift_vel
        pos_list = []
        vel_list = []
        for i in range(1, self.time_range):
            pos, vel = self.rk4(tmp_pos, tmp_vel, self.time_step)
            pos_list.append(pos)
            vel_list.append(vel)
            tmp_pos = pos
            tmp_vel = vel

        print("\nPosition : ")
        for i, j in enumerate(pos_list):
            print("----------------")
            print(f"state {i} : \n{j}")

        print("\nRadial Velocity: ")
        for i, j in enumerate(vel_list):
            print("----------------")
            print(f"state {i} : \n{j}")


        self.result_pos = pos_list
        self.result_vel = vel_list


    def plot_result(self):
        plt_pos = np.empty((self.time_range, self.pos.shape[0], self.pos.shape[1]))
        plt_vel = np.empty((self.time_range, self.pos.shape[0], self.pos.shape[1]))

        tmp_pos = self.shift_pos
        tmp_vel = self.shift_vel

        for i in range(1, self.time_range):
            pos, vel = self.rk4(tmp_pos, tmp_vel, self.time_step)
            plt_pos[i] = pos
            plt_vel[i] = vel
            tmp_pos = pos
            tmp_vel = vel

        fig = plt.figure(figsize=(13, 13))
        ax = fig.add_subplot()
        for i in list(range(plt_pos.shape[1])):
            ax.plot(plt_pos[:, i, 0], plt_pos[:, i, 1], ".", alpha=0.5, label=self.names[i])
            ax.scatter(plt_pos[-1, i, 0], plt_pos[-1, i, 1], marker="o", label=f"{i}")

        plt.legend()
        plt.axis("equal")
        plt.grid()
        plt.show()


if __name__ == "__main__":

    AU = 1.496e11
    sec_in_day = 24 * 3600
    t = 36500 * sec_in_day
    dt = 100 * sec_in_day

    alpha_centauri_A = Star("A", [0.0, 0.0, 0.0], [0.0, 2234.5, 0.0], 1.1*1.989e30)
    alpha_centauri_B = Star("B", [23*AU, 0.0, 0.0], [0.0, -1810, 0.0], 0.907*1.989e30)

    Test = Simulation(stars=[alpha_centauri_A, alpha_centauri_B], t=t, dt=dt)
    Test.shift_pos_vel()
    Test.plot_result()
    Test.result_data()







