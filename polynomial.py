# 多项式类
class Polynomial:
    def __init__(self,coefficients):
        # 升幂排列
        self.coefficients = coefficients
        self.degree = len(coefficients) - 1
        self.integral = None

    def __call__(self,x):
        res = 0
        # 改用秦九韶算法
        # 
        for i in range(self.degree,-1,-1):
            res = res * x + self.coefficients[i]        
        return res
    
    def __str__(self):
        s = ""
        for i in range(self.degree+1):
            s += f"{self.coefficients[i]}x^{i} + "
        s = s[:-3]
        return s
    
    def diff(self):
        if self.degree == 0:
            return Polynomial([0])
        else:
            new_coefficients = [self.coefficients[i] * i for i in range(1, self.degree + 1)]
            return Polynomial(new_coefficients)
        
    def integral(self):
        if self.integral is not None:
            return self.integral
        new_coefficients = [0] + [self.coefficients[i] / (i + 1) for i in range(self.degree + 1)]
        self.integral = Polynomial(new_coefficients)

        return self.integral
    
    def definite_integral(self,a,b):
        integral_poly = self.integral()
        return integral_poly(b) - integral_poly(a)