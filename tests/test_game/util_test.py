import game.utils as utils


def test_distance__x_only():
    assert utils.distance((0.0, 0.0), (1.0, 0.0)) == 1


def test_distance__y_only():
    assert utils.distance((0.0, 0.0), (0.0, 7.3)) == 7.3


def test_distance__diagonal():
    rounded = "{:.4f}".format(utils.distance((100.0, -3.2), (-0.750, 34.0)))
    assert rounded == '107.3983'


def test_normalize_degrees__noop():
    rounded = "{:.4f}".format(utils.normalize_degrees(97.5))
    assert rounded == '97.5000'


def test_normalize_degrees__negative():
    rounded = "{:.4f}".format(utils.normalize_degrees(-134.234))
    assert rounded == '225.7660'


def test_normalize_degrees__positive_overflow():
    rounded = "{:.4f}".format(utils.normalize_degrees(465.345))
    assert rounded == '105.3450'


def test_normalize_degrees__negative_overflow():
    rounded = "{:.4f}".format(utils.normalize_degrees(-1785.0))
    assert rounded == '15.0000'
