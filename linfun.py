class LinFun:
    # Linear function f(x) = ax + b
    def __init__(self, a, b):
        self._a, self._b = a, b
        self.hasZero = a != 0 or b == 0
    def zero(self):
        return -self._b / self._a # what if a == b == 0 ?
    def eval(self, x):
        return self._a * x + self._b
    def __add__(self, other):
        return LinFun(self._a + other._a, self._b + other._b)

# f = LinFun(0.5, -2)                  # f(x) = 0.5x - 2
# print(f.hasZero)                     # True
# print(f.zero())                      # 4.0
# print(f.eval(f.zero()))              # 0.0 (phew!)
# print((f + LinFun(-0.5, 3)).hasZero) # False