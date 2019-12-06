import numpy as np 

class Variables() :

    def __init__(self) :
        # self.xb = set()
        # self.xt = set()
        # self.yb = set()
        # self.yt = set()
        # self.zb = set()
        # self.zt = set()
        self.slots = []

    def get_vars(self) :
        # return [self.xb, self.xt, self.yb, self.yt, self.zb, self.zt]
        return self.slots

    def set_vars(self, n) :
        # self.xb = xb
        # self.xt = xt
        # self.yb = yb
        # self.yt = yt
        # self.zb = zb
        # self.zt = zt
        print(n)
        self.slots = np.zeros((n,))

    def set_var(self, index, incr) :
        self.slots[index] += incr

    # def get_vars(self) :
    #     return [self.xb, self.xt, self.yb, self.yt, self.zb, self.zt]

    # def set_vars(self, xb, xt, yb, yt, zb, zt) :
    #     self.xb = xb
    #     self.xt = xt
    #     self.yb = yb
    #     self.yt = yt
    #     self.zb = zb
    #     self.zt = zt