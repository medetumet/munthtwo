class Add:
    def __init__(self, add):
        self.add = add

    def __add__(self, other):
        return self.add + other.add


class Sub:
    def __init__(self, sub):
        self.sub = sub

    def __sub__(self, other):
        return self.sub - other.sub


class Mul:
    def __init__(self, mul):
        self.mul = mul

    def __mul__(self, other):
        return self.mul * other.mul


class TrueDiv:
    def __init__(self, truediv):
        self.truediv = truediv

    def __truediv__(self, other):
        return self.truediv / other.truediv


class Calculator(Add, Sub, Mul, TrueDiv):
    def __init__(self, val):
        Add.__init__(self, val)
        Sub.__init__(self, val)
        Mul.__init__(self, val)
        TrueDiv.__init__(self, val)


first_number = Calculator(2)
second_number = Calculator(5)

print(f'{first_number+second_number}\n'
      f'{first_number-second_number}\n'
      f'{first_number*second_number}\n'
      f'{first_number/second_number}\n')

