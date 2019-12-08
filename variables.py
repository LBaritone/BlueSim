import numpy as np 

class Variables() :

    def __init__(self) :
        self.slots = []

    def get_vars(self) :
        return self.slots

    def set_vars(self, shape) :

        print(shape)
        a, b, c, _ = shape
        self.slots = np.zeros((a, b, c))

    def set_var(self, index, incr) :
        a, b, c = index
        self.slots[a, b, c] += incr

