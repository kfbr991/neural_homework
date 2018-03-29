import numpy as np


class Neuron:
    def __init__(self, Q, w):
        self.Q = Q
        self.w = w
        self.y = 0

    def cacl_y(self, x):
        self.y = self.sigma(np.sum(np.multiply(x, self.w)) - self.Q)

    def sigma(self, z):
        return 1/(1+np.exp(-z))
