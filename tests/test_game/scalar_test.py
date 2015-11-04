from tests.utils import eq_within_epsilon
from game.scalar import Scalar


def test_init__simple():
    sut = Scalar(5)

    assert sut.value == 5
    assert sut.max == 5
    assert sut.min == 0
    assert sut.fraction == 1.0


def test_init__and_max():
    sut = Scalar(4, max=12)

    assert sut.value == 4
    assert sut.max == 12
    assert sut.min == 0
    assert sut.fraction == (1.0 / 3.0)


def test_init__and_min():
    sut = Scalar(6.3, min=4.23)

    assert sut.value == 6.3
    assert sut.max == 6.3
    assert sut.min == 4.23
    assert sut.fraction == 1.0


def test_init__max_and_min():
    sut = Scalar(12.75, max=34.23, min=-12.65)

    assert sut.value == 12.75
    assert sut.max == 34.23
    assert sut.min == -12.65
    assert eq_within_epsilon(sut.fraction, 0.5416)


def test_init__negative():
    sut = Scalar(-5)

    assert sut.value == -5
    assert sut.max == 0
    assert sut.min == -5
    assert sut.fraction == 0.0


def test_init__negative_max():
    sut = Scalar(-4, max=-12)

    assert sut.value == -4
    assert sut.max == 0
    assert sut.min == -12
    assert sut.fraction == (2.0 / 3.0)


def test_init__negative_min():
    sut = Scalar(6, min=-7)

    assert sut.value == 6
    assert sut.max == 6
    assert sut.min == -7
    assert sut.fraction == 1.0


def test_init__switched_max_and_min():
    sut = Scalar(5, max=3, min=8)

    assert sut.value == 5
    assert sut.max == 8
    assert sut.min == 3
    assert sut.fraction == 0.4


def test_convert__string():
    sut = Scalar(4)
    assert str(sut) == "4.0"


def test_convert__string_decimal():
    sut = Scalar(4.345)
    assert str(sut) == "4.345"


def test_convert__int():
    sut = Scalar(3)
    assert int(sut) == 3


def test_convert__int_decimal():
    sut = Scalar(3.23)
    assert int(sut) == 3


def test_convert__float():
    sut = Scalar(3)
    assert float(sut) == 3


def test_convert__float_decimal():
    sut = Scalar(3.23)
    assert float(sut) == 3.23
