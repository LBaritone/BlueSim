

class Variables() :

    def __init__(self) :
        self.xb = set()
        self.xt = set()
        self.yb = set()
        self.yt = set()
        self.zb = set()
        self.zt = set()

    def get_vars(self) :
        return [self.xb, self.xt, self.yb, self.yt, self.zb, self.zt]

    def set_vars(self, xb, xt, yb, yt, zb, zt) :
        self.xb = xb
        self.xt = xt
        self.yb = yb
        self.yt = yt
        self.zb = zb
        self.zt = zt