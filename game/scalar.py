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

        self.value = current

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value > self.max:
            value = self.max

        if value < self.min:
            value = self.min

        self._value = float(value)

    @property
    def fraction(self):
        numerator = self._value - self.min
        denominator = self.max - self.min

        if denominator == 0 and numerator == 0:
            if self._value == 0:
                return 0.0
            else:
                return 1.0
        else:
            return numerator / denominator

    def __str__(self):
        string = str(self._value) + "/"
        if self.min != 0:
            string += "[" + str(self.min) + "," + str(self.max) + "]"
        else:
            string += str(self.max)
        return string

    def __repr__(self):
        string = "Scalar(" + str(self._value)
        string += ", max=" + str(self.max)
        string += ", min=" + str(self.min)
        string += ")"
        return string

    def __int__(self):
        return int(self._value)

    def __float__(self):
        return float(self._value)

    def __add__(self, other):
        return self._value + other

    def __radd__(self, other):
        return other + self._value

    def __sub__(self, other):
        return self._value - other

    def __rsub__(self, other):
        return other - self._value

    def __mul__(self, other):
        return self._value * other

    def __rmul__(self, other):
        return other * self._value

    def __div__(self, other):
        return self._value / other

    def __rdiv__(self, other):
        return other / self._value

    def __lt__(self, other):
        return self._value < other

    def __gt__(self, other):
        return self._value > other

    def __le__(self, other):
        return self._value <= other

    def __ge__(self, other):
        return self._value >= other

    def __eq__(self, other):
        return self._value == other

    def __ne__(self, other):
        return self._value != other

    def __nonzero__(self):
        return True if self._value != 0 else False

    def __abs__(self):
        return abs(self._value)

    def __floordiv__(self, other):
        return self._value // other

    def __rfloordiv__(self, other):
        return other // self._value

    def __index__(self):
        raise NotImplementedError

    def __neg__(self):
        return -self._value

    def __mod__(self, other):
        raise NotImplementedError

    def __pow__(self, other):
        raise NotImplementedError
