from tests.utils import eq_within_epsilon
from game.scalar import Scalar


# init tests
def test_init__simple():
    sut = Scalar(5)

    assert sut.value == 5
    assert sut.max == 5
    assert sut.min == 0


def test_init__and_max():
    sut = Scalar(4, max=12)

    assert sut.value == 4
    assert sut.max == 12
    assert sut.min == 0


def test_init__and_min():
    sut = Scalar(6.3, min=4.23)

    assert sut.value == 6.3
    assert sut.max == 6.3
    assert sut.min == 4.23


def test_init__max_and_min():
    sut = Scalar(12.75, max=34.23, min=-12.65)

    assert sut.value == 12.75
    assert sut.max == 34.23
    assert sut.min == -12.65


def test_init__negative():
    sut = Scalar(-5)

    assert sut.value == -5
    assert sut.max == 0
    assert sut.min == -5


def test_init__negative_max():
    sut = Scalar(-14, max=-12)

    assert sut.value == -14
    assert sut.max == -12
    assert sut.min == -14


def test_init__negative_min():
    sut = Scalar(6, min=-7)

    assert sut.value == 6
    assert sut.max == 6
    assert sut.min == -7


def test_init__switched_max_and_min():
    try:
        Scalar(5, max=3, min=8)
    except ValueError as err:
        assert err.message == "max must be >= min"
    else:
        assert False


def test_init__zero():
    sut = Scalar(0)

    assert sut.value == 0
    assert sut.max == 0
    assert sut.min == 0


def test_init__zero_denominator():
    sut = Scalar(5, min=5, max=5)

    assert sut.value == 5.0
    assert sut.max == 5.0
    assert sut.min == 5.0


def test_init__value_out_of_bounds():
    sut = Scalar(17, min=5, max=10)

    assert sut.value == 10
    assert sut.max == 10
    assert sut.min == 5


# set tests
def test_set_value__normal():
    sut = Scalar(8)

    sut.value = 5

    assert sut.value == 5


def test_set_value__too_low():
    sut = Scalar(4)

    sut.value = -3.5

    assert sut.value == 0


def test_set_value__too_high():
    sut = Scalar(6)

    sut.value = 9

    assert sut.value == 6


def test_set_min__normal():
    sut = Scalar(9)

    sut.min = 3

    assert sut.value == 9
    assert sut.min == 3


def test_set_min__higher_than_value():
    sut = Scalar(5, max=10)

    sut.min = 7

    assert sut.value == 7
    assert sut.min == 7


def test_set_min__higher_than_max():
    sut = Scalar(5)

    try:
        sut.min = 7
    except ValueError as err:
        assert err.message == "min must be <= max"
    else:
        assert False


def test_set_max__normal():
    sut = Scalar(4)

    sut.max = 7

    assert sut.value == 4
    assert sut.max == 7


def test_set_max__lower_than_value():
    sut = Scalar(7)

    sut.max = 4

    assert sut.value == 4
    assert sut.max == 4


def test_set_max__lower_than_min():
    sut = Scalar(5)

    try:
        sut.max = -2
    except ValueError as err:
        assert err.message == 'max must be >= min'
    else:
        assert False


# fraction tests
def test_fraction__full():
    sut = Scalar(4)

    assert sut.fraction == 1.0


def test_fraction__full_and_changed():
    sut = Scalar(7, max=10)

    assert sut.fraction == 0.7

    sut.value = 10

    assert sut.fraction == 1.0


def test_fraction__messy():
    sut = Scalar(34, max=145)

    assert eq_within_epsilon(sut.fraction, 0.23)


def test_fraction__all_zero():
    sut = Scalar(0, max=0, min=0)

    assert sut.fraction == 0


def test_fraction__no_range():
    sut = Scalar(5, max=5, min=5)

    assert sut.fraction == 1


# conversion tests
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


# addition(+) tests
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


# subtraction(-) tests
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


# multiplication(*) tests
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


# division(/) tests
def test_divide__scalar_int():
    sut = Scalar(3)

    assert sut / 2 == 1.5


def test_divide__float_scalar_int():
    sut = Scalar(3.33)

    assert eq_within_epsilon(sut / 3, 1.11)


def test_divide__scalar_float():
    sut = Scalar(7)

    assert sut / 2.5 == 2.8


def test_divide__float_scalar():
    sut = Scalar(2.5)

    assert 7.5 / sut == 3.0


def test_divide__int_scalar():
    sut = Scalar(3)

    assert eq_within_epsilon(2 / sut, 0.66)


def test_divide__int_float_scalar():
    sut = Scalar(1.5)

    assert eq_within_epsilon(5 / sut, 3.33)


def test_divide__scalar_scalar():
    sut = Scalar(6)
    sut2 = Scalar(3)

    assert sut / sut2 == 2


def test_divide__float_scalar_scalar():
    sut = Scalar(7.5)
    sut2 = Scalar(3)

    assert sut / sut2 == 2.5


def test_divide__scalar_float_scalar():
    sut = Scalar(3)
    sut2 = Scalar(0.5)

    assert sut / sut2 == 6


def test_divide__scalar_by_zero():
    sut = Scalar(2)
    try:
        sut / 0
    except ZeroDivisionError:
        assert True
    else:
        assert False


def test_divide__by_zero_scalar():
    sut = Scalar(0)
    try:
        5 / sut
    except ZeroDivisionError:
        assert True
    else:
        assert False


# floordiv tests
def test_floor_divide__scalar_int():
    sut = Scalar(3)

    assert sut // 2 == 1


def test_floor_divide__float_scalar_int():
    sut = Scalar(3.33)

    assert eq_within_epsilon(sut // 3, 1)


def test_floor_divide__scalar_float():
    sut = Scalar(7)

    assert sut // 2.5 == 2


def test_floor_divide__float_scalar():
    sut = Scalar(2.5)

    assert 7.5 // sut == 3


def test_floor_divide__int_scalar():
    sut = Scalar(3)

    assert eq_within_epsilon(2 // sut, 0)


def test_floor_divide__int_float_scalar():
    sut = Scalar(1.5)

    assert eq_within_epsilon(5 // sut, 3)


def test_floor_divide__scalar_scalar():
    sut = Scalar(6)
    sut2 = Scalar(3)

    assert sut // sut2 == 2


def test_floor_divide__float_scalar_scalar():
    sut = Scalar(7.5)
    sut2 = Scalar(3)

    assert sut // sut2 == 2


def test_floor_divide__scalar_float_scalar():
    sut = Scalar(3)
    sut2 = Scalar(0.5)

    assert sut // sut2 == 6


def test_floor_divide__scalar_by_zero():
    sut = Scalar(2)
    try:
        sut // 0
    except ZeroDivisionError:
        assert True
    else:
        assert False


def test_floor_divide__by_zero_scalar():
    sut = Scalar(0)
    try:
        5 // sut
    except ZeroDivisionError:
        assert True
    else:
        assert False


# less-than(<) tests
def test_less_than__first_and_true():
    sut = Scalar(4)

    assert sut < 6


def test_less_than__first_and_false():
    sut = Scalar(3)

    assert not (sut < 2)


def test_less_than__second_and_true():
    sut = Scalar(4)

    assert 3 < sut


def test_less_than__second_and_false():
    sut = Scalar(3)

    assert not (5 < sut)


# greater-than(>) tests
def test_greater_than__first_and_true():
    sut = Scalar(7)

    assert sut > 6


def test_greater_than__first_and_false():
    sut = Scalar(3)

    assert not (sut > 4)


def test_greater_than__second_and_true():
    sut = Scalar(2)

    assert 3 > sut


def test_greater_than__second_and_false():
    sut = Scalar(7)

    assert not (5 > sut)


# less-than-or-equal(<-) tests
def test_less_than_or_equal__first_and_true():
    sut = Scalar(4)

    assert sut <= 6


def test_less_than_or_equal__first_and_equal():
    sut = Scalar(6)

    assert sut <= 6


def test_less_than_or_equal__first_and_equal_with_float():
    sut = Scalar(12)

    assert sut <= 12.0


def test_less_than_or_equal__first_and_equal_with_float_scalar():
    sut = Scalar(2.0)

    assert sut <= 2


def test_less_than_or_equal__first_and_false():
    sut = Scalar(3)

    assert not (sut <= 2)


def test_less_than_or_equal__second_and_true():
    sut = Scalar(4)

    assert 3 <= sut


def test_less_than_or_equal__second_and_equal():
    sut = Scalar(6)

    assert 6 <= sut


def test_less_than_or_equal__second_and_equal_with_float():
    sut = Scalar(8)

    assert 8.0 <= sut


def test_less_than_or_equal__second_and_equal_with_float_scalar():
    sut = Scalar(3.0)

    assert 3 <= sut


def test_less_than_or_equal__second_and_false():
    sut = Scalar(3)

    assert not (5 <= sut)


# gretaer-than-or-equal(>=) tests
def test_greater_than_or_equal__first_and_true():
    sut = Scalar(91)

    assert sut >= 6


def test_greater_than_or_equal__first_and_equal():
    sut = Scalar(44)

    assert sut >= 44


def test_greater_than_or_equal__first_and_equal_with_float():
    sut = Scalar(34)

    assert sut >= 34.0


def test_greater_than_or_equal__first_and_equal_with_float_scalar():
    sut = Scalar(-47.0)

    assert sut >= -47


def test_greater_than_or_equal__first_and_false():
    sut = Scalar(-35)

    assert not (sut >= 205)


def test_greater_than_or_equal__second_and_true():
    sut = Scalar(67)

    assert 67 >= sut


def test_greater_than_or_equal__second_and_equal():
    sut = Scalar(26)

    assert 26 >= sut


def test_greater_than_or_equal__second_and_equal_with_float():
    sut = Scalar(-28)

    assert -28.0 >= sut


def test_greater_than_or_equal__second_and_equal_with_float_scalar():
    sut = Scalar(333.0)

    assert 333 >= sut


def test_greater_than_or_equal__second_and_false():
    sut = Scalar(32)

    assert not (-5 >= sut)


# equality(==) tests
def test_equality__equal():
    sut = Scalar(3)

    assert sut == 3


def test_equality__not_equal():
    sut = Scalar(7)

    assert not (sut == 3)


def test_equality__equal_left():
    sut = Scalar(3)

    assert 3 == sut


def test_equality__not_equal_left():
    sut = Scalar(7)

    assert not (3 == sut)


# inequality(!=) tests
def test_inequality__equal():
    sut = Scalar(71)

    assert not (sut != 71)


def test_inequality__not_equal():
    sut = Scalar(12)

    assert sut != -543


def test_inequality__equal_left():
    sut = Scalar(72.24)

    assert not (72.24 != sut)


def test_inequality__not_equal_left():
    sut = Scalar(2345)

    assert 0.2346 != sut


# truthy tests
def test_nonzero__nonzero():
    sut = Scalar(3)

    assert sut


def test_nonzero__zero():
    sut = Scalar(0)

    assert not sut


# abs tests
def test_abs__positive():
    sut = Scalar(2.5)

    assert abs(sut) == 2.5


def test_abs_negative():
    sut = Scalar(-15.67)

    assert abs(sut) == 15.67


# negation tests
def test_negate__positive():
    sut = Scalar(5)

    assert -sut == -5


def test_negate__negative():
    sut = Scalar(-234.23)

    assert -sut == 234.23


# TODO: mod tests
def test_modulo__zero():
    sut = Scalar(4)

    assert sut % 2 == 0


def test_modulo__two():
    sut = Scalar(8)

    assert sut % 3 == 2


def test_modulo__float():
    sut = Scalar(2.5)

    assert sut % 1 == 0.5


def test_modulo__zero_reverse():
    sut = Scalar(2)

    assert 6 % sut == 0


def test_modulo__three_reverse():
    sut = Scalar(4)

    assert 11 % sut == 3


def test_modulo__float_reverse():
    sut = Scalar(1.25)

    assert 6.5 % sut == 0.25


# TODO: pow tests
