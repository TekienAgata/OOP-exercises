# import pytest
from L1Ex3 import Dice


def test_dice():
    d1 = Dice(6)
    assert d1._Dice__sides == 6
    assert d1._value is None


def test_roll():
    d1 = Dice(6)
    d1.roll()
    assert d1._value in [1, 2, 3, 4, 5, 6]


def test_get_sides():
    d1 = Dice(15)
    assert d1.get_sides() == 15


def test_get_value():
    d1 = Dice(72)
    assert d1.get_value() is None


def test_str(capsys):
    d1 = Dice(6)
    assert str(d1).strip() == "Sides = 6, value not set"
