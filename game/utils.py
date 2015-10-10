import math


def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between 2 points"""
    return math.sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2)


def normalize_degrees(angle):
    magnitude = angle
    direction = 1.0
    if magnitude < 0:
        direction = -1
        magnitude *= direction
    magnitude %= 360.0
    magnitude *= direction

    if magnitude < 0:
        magnitude = 360.0 + magnitude

    return magnitude
