def fps_to_s(fps):
    return 1.0 / fps


def eq_within_epsilon(value, expected, epsilon=0.01):
    return abs(expected - value) < epsilon
