import numpy as np


class XorNeuron:
    def __init__(self, x1, x2):
        self.Q = 0
        self.w = [1, 1]
        self.y = self.cacl_y(x1, x2)


    def cacl_y(self, x1, x2):
        return self.sigma(np.sum(np.multiply(self.w, [x1, x2])) - self.Q)

    def sigma(self, a):
        if a > 0:
            return 1
        return 0
