class Scalar(object):
    def __init__(self, current, max=None, min=None):
        self._min = None
        self._max = None
        self._value = None

        if max is None:
            max = 0.0 if current < 0 else current
        if min is None:
            min = 0.0 if current > 0 else current

        self.min = min
        self.max = max

        self.value = current

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value > self._max:
            value = self._max

        if value < self._min:
            value = self._min

        self._value = float(value)

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, value):
        if self._max is not None and value > self._max:
            raise ValueError("min must be <= max")

        self._min = float(value)

        if self._value < self._min:
            self._value = value

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        if self._min is not None and value < self._min:
            raise ValueError("max must be >= min")

        self._max = float(value)

        if self._value > self._max:
            self._value = value

    @property
    def fraction(self):
        numerator = self._value - self._min
        denominator = self._max - self._min

        if denominator == 0 and numerator == 0:
            if self._value == 0:
                return 0.0
            else:
                return 1.0
        else:
            return numerator / denominator

    def __str__(self):
        string = str(self._value) + "/"
        if self._min != 0:
            string += "[" + str(self._min) + "," + str(self._max) + "]"
        else:
            string += str(self._max)
        return string

    def __repr__(self):
        string = "Scalar(" + str(self._value)
        string += ", max=" + str(self._max)
        string += ", min=" + str(self._min)
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

    def __neg__(self):
        return -self._value

    def __mod__(self, other):
        return self._value % other

    def __rmod__(self, other):
        return other % self._value

    def __pow__(self, other):
        raise NotImplementedError
