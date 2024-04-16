import pytest

from L1Ex1 import Coin, coin_game


def test_coin_init():
    coin1 = Coin(5)
    assert coin1.side == "heads"
    assert coin1.denomination == 5


def test_coin_lacking_init():
    """
    To test if initiating a coin without
    denomination produces an error
    """
    with pytest.raises(TypeError):
        coin1 = Coin()


def test_coin_throw():
    coin1 = Coin(1)
    coin1.throw()
    assert coin1.side in ["heads", "tails"]


def test_str():
    coin1 = Coin(5)
    assert str(coin1) == ("Coin's side: heads, " "coin's denomination: 5")


def test_coin_game():
    wins = 0
    for _ in range(100):
        if coin_game() is True:
            wins += 1
    assert 10 < wins < 35
