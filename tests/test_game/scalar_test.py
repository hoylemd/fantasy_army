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


def test_init__zero():
    sut = Scalar(0)

    assert sut.value == 0
    assert sut.max == 0
    assert sut.min == 0
    assert sut.fraction == 0


def test_convert__string_simple():
    sut = Scalar(4)
    assert str(sut) == "4.0/4.0"


def test_convert__string_partial():
    sut = Scalar(3, max=7.5)
    assert str(sut) == "3.0/7.5"


def test_convert__string_complex():
    sut = Scalar(2, min=-1, max=20)
    assert str(sut) == "2.0/[-1.0,20.0]"


def test_convert__repr():
    sut = Scalar(4.345)
    assert repr(sut) == "Scalar(4.345, max=4.345, min=0.0)"


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


def test_add__scalar_int():
    sut = Scalar(3)

    assert sut + 2 == 5


def test_add__float_scalar_int():
    sut = Scalar(3.33)

    assert sut + 3 == 6.33


def test_add__scalar_float():
    sut = Scalar(7)

    assert sut + 23.65 == 30.65


def test_add__float_scalar():
    sut = Scalar(2.5)

    assert 7.5 + sut == 10.0


def test_add__int_scalar():
    sut = Scalar(3)

    assert 2 + sut == 5


def test_add__int_float_scalar():
    sut = Scalar(3.4)

    assert 5 + sut == 8.4


def test_add__scalar_scalar():
    sut = Scalar(3)
    sut2 = Scalar(6)

    assert sut + sut2 == 9


def test_add__float_scalar_scalar():
    sut = Scalar(1.25)
    sut2 = Scalar(4)

    assert sut + sut2 == 5.25


def test_add__scalar_float_scalar():
    sut = Scalar(3)
    sut2 = Scalar(4.9)

    assert sut + sut2 == 7.9


def test_subtract__scalar_int():
    sut = Scalar(3)

    assert sut - 2 == 1


def test_subtract__float_scalar_int():
    sut = Scalar(3.33)

    assert eq_within_epsilon(sut - 3, 0.33)


def test_subtract__scalar_float():
    sut = Scalar(7)

    assert sut - 23.65 == -16.65


def test_subtract__float_scalar():
    sut = Scalar(2.5)

    assert 7.5 - sut == 5


def test_subtract__int_scalar():
    sut = Scalar(3)

    assert 2 - sut == -1


def test_subtract__int_float_scalar():
    sut = Scalar(3.4)

    assert 5 - sut == 1.6


def test_subtract__scalar_scalar():
    sut = Scalar(3)
    sut2 = Scalar(6)

    assert sut - sut2 == -3


def test_subtract__float_scalar_scalar():
    sut = Scalar(1.25)
    sut2 = Scalar(4)

    assert sut - sut2 == -2.75


def test_subtract__scalar_float_scalar():
    sut = Scalar(3)
    sut2 = Scalar(4.9)

    assert eq_within_epsilon(sut - sut2, -1.9)


def test_multiply__scalar_int():
    sut = Scalar(3)

    assert sut * 2 == 6


def test_multiply__float_scalar_int():
    sut = Scalar(3.33)

    assert eq_within_epsilon(sut * 3, 9.99)


def test_multiply__scalar_float():
    sut = Scalar(7)

    assert sut * 2.5 == 17.5


def test_multiply__float_scalar():
    sut = Scalar(2.5)

    assert 7.5 * sut == 18.75


def test_multiply__int_scalar():
    sut = Scalar(3)

    assert 2 * sut == 6


def test_multiply__int_float_scalar():
    sut = Scalar(3.4)

    assert 5 * sut == 17.0


def test_multiply__scalar_scalar():
    sut = Scalar(3)
    sut2 = Scalar(6)

    assert sut * sut2 == 18


def test_multiply__float_scalar_scalar():
    sut = Scalar(1.25)
    sut2 = Scalar(3)

    assert sut * sut2 == 3.75


def test_multiply__scalar_float_scalar():
    sut = Scalar(3)
    sut2 = Scalar(4.2)

    assert eq_within_epsilon(sut * sut2, 12.6)
