import math


class S:
    def __init__(self, x):
        self.x = x

    def calculate(self, n):
        numerator = (-1)**n * self.x**(2*n)
        denominator = math.factorial(2*n)
        return numerator / denominator


# tmp = int(input())
n = int(input())
s = S(3)  # khởi tạo đối tượng S với x = 3
for i in range(1, n):
    print(s.calculate(i))
# day chi la test chuc nang
