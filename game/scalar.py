import numbers


class Scalar(object):
    def __init__(self, current, max=None, min=None):
        if max is None:
            self.max = float(current)
        else:
            self.max = float(max)

        if min is None:
            self.min = float(0)
        else:
            self.min = float(min)

        if self.max < self.min:
            self.min, self.max = self.max, self.min

        self.set(current)

    def set(self, value):
        if value > self.max:
            value = self.max

        if value < self.min:
            value = self.min

        self.value = float(value)
        self._calc_fraction()

    def _calc_fraction(self):
        numerator = self.value - self.min
        denominator = self.max - self.min

        self.fraction = numerator / denominator

    def __str__(self):
        string = str(self.value) + "/"
        if self.min != 0:
            string += "[" + str(self.min) + "," + str(self.max) + "]"
        else:
            string += str(self.max)
        return string

    def __repr__(self):
        string = "Scalar(" + str(self.value)
        string += ", max=" + str(self.max)
        string += ", min=" + str(self.min)
        string += ")"
        return string

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        operand = self.value
        if isinstance(other, numbers.Integral):
            operand = int(self.value)
        return other + operand
