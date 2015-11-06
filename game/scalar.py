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

        if denominator == 0 and numerator == 0:
            if self.value == 0:
                self.fraction = 0.0
            else:
                self.fraction = 1.0
        else:
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
        return other + self.value

    def __sub__(self, other):
        return self.value - other

    def __rsub__(self, other):
        return other - self.value

    def __mul__(self, other):
        return self.value * other

    def __rmul__(self, other):
        return other * self.value

    def __div__(self, other):
        return self.value / other

    def __rdiv__(self, other):
        return other / self.value

    def __lt__(self, other):
        return self.value < other

    def __gt__(self, other):
        return self.value > other

    def __le__(self, other):
        return self.value <= other

    def __ge__(self, other):
        return self.value >= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __nonzero__(self):
        return True if self.value != 0 else False

    def __abs__(self):
        return abs(self.value)
