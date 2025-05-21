# y'(x) = f(x,y)
# y'(x_0) = y_0

class Ode:
    def __init__(self,dy:callable,f:callable,x,y):
        self.dy = dy
        self.f = f
        self.init = (x,y)

    