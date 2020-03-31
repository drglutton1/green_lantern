import pytest


def func(x):
    return x + 2


def test_answer():
    assert func(3) == 5


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as err:
        1 / 0


