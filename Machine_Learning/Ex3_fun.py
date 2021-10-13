import numpy as np
import matplotlib.pyplot as plt


def sigm(x):
    return 1.0 / (1 + np.exp(-x))

def sigm_deriv(x):
    return (1.0 / (1 + np.exp(-x))) * (1 - (1.0 / (1 + np.exp(-x))))



def tanh(x):
    return np.tanh(x)

def tanh_deriv(x):
    return 1.0 - np.tan(x) * np.tan(x)


def relu(x):
    if x.all() >= 0:
        return x
    else:
        return 0

def relu_deriv(x):
    if x.all() >= 0:
        return 1
    else:
        return 0



