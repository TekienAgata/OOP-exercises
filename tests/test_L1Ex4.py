import pytest

from L1Ex4 import Account


def test_account():
    a1 = Account(12, "Anna Blabla")
    assert a1.balance == 12
    assert a1.name == "Anna Blabla"


def test_account_negative_balance():
    with pytest.raises(ValueError) as err:
        a1 = Account(-3, "Anna Bleble")
    assert str(err.value) == "Balance cannot be negative"


def test_deposit():
    a1 = Account(8, "Anna Blibli")
    a1.deposit(12)
    assert a1.balance == 20


def test_deposit_negative_amount():
    a1 = Account(52, "Anna Blublu")
    with pytest.raises(ValueError) as err:
        a1.deposit(-2)
    assert str(err.value) == "Cannot deposit negative amount"


def test_take():
    a1 = Account(101, "Anna Bloblo")
    a1.take(2)
    assert a1.balance == 99


def test_take_too_much():
    a1 = Account(12, "Anna Blybly")
    with pytest.raises(ValueError) as err:
        a1.take(99999999)
    assert str(err.value) == "Not enough balance"
