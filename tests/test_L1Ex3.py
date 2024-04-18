import pytest

from L1Ex3 import BlackJack, Dice


def test_dice():
    d1 = Dice(6)
    assert d1.get_sides() == 6
    assert d1._value is None


def test_roll():
    d1 = Dice(6)
    d1.roll()
    assert d1.get_value() in [1, 2, 3, 4, 5, 6]


def test_get_sides():
    d1 = Dice(15)
    assert d1.get_sides() == 15


def test_get_value():
    d1 = Dice(72)
    assert d1.get_value() is None


def test_str():
    d1 = Dice(6)
    assert str(d1).strip() == "Sides = 6, value not set"


def test_blackjack_computer():
    testing = BlackJack()
    testing.throw_computer()
    assert testing.computer_result > 1


def test_blackjack_player(monkeypatch):
    mock_answer = ["no", "yes"]
    monkeypatch.setattr("builtins.input", lambda _: mock_answer.pop())
    testing = BlackJack()
    testing.game()
    assert testing.player_result < 0 or testing.player_result >= 21


@pytest.mark.parametrize(
    "computer, player, outcome",
    [
        (21, 21, "it's a tie"),
        (18, 12, "computer wins"),
        (17, 19, "player wins"),
        (17, 23, "computer wins"),
    ],
)
def test_who_wins(computer, player, outcome):
    testing = BlackJack()
    testing.computer_result = computer
    testing.player_result = player
    assert testing.who_wins() == outcome
