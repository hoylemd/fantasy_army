
class Scalar(object):
    def __init__(self, current_value, max_value=None, min_value=None):
        if max_value is None:
            self.max_value = float(current_value)
        else:
            self.max_value = float(max_value)

        if min_value is None:
            self.min_value = float(0)
        else:
            self.min_value = float(min_value)

        if self.max_value < self.min_value:
            self.min_value, self.max_value = self.max_value, self.min_value

        self.set_value(current_value)

    def set_value(self, value):
        if value > self.max_value:
            value = self.max_value

        if value < self.min_value:
            value = self.min_value

        self.value = float(value)
        self._calc_fraction()

    def _calc_fraction(self):
        numerator = self.value - self.min_value
        denominator = self.max_value - self.min_value

        self.fraction = numerator / denominator
