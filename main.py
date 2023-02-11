class Coder1:
    def __init__(self):
        self.a = int(input("Number A - "))
        self.b = int(input("Number B - "))

    def ret_numb(self):
        c = int(self.a + self.b)
        d = int(self.a - self.b)
        return c * d


class Coder2:
    def __init__(self, c):
        self.d = c / 2
    def ret_numb(self):
        return self.d


math = Coder1()
math2 = Coder2(math.ret_numb())
print(math2.ret_numb())
