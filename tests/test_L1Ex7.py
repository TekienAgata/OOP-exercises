import pytest

from L1Ex7 import Pet


def test_pet_init():
    p1 = Pet("Reksio")
    assert p1.name == "Reksio"
    assert p1.hunger == 0
    assert p1.tiredness == 0


def test_name_too_short():
    with pytest.raises(ValueError) as err:
        p1 = Pet("Re")
    assert str(err.value) == "Name too short"


def test_name_invalid_characters_used_int():
    with pytest.raises(ValueError) as err:
        p1 = Pet("Reksio1")
    assert str(err.value) == "Invalid characters used"


def test_name_invalid_characters_used_comma():
    with pytest.raises(ValueError) as err:
        p1 = Pet("Rek,sio")
    assert str(err.value) == "Invalid characters used"


def test_passage_of_time():
    p1 = Pet("Reksio")
    p1._passage_of_time()
    assert p1.tiredness == 1
    assert p1.hunger == 1


def test_21_passage_of_time():
    p1 = Pet("Reksio")
    for _ in range(21):
        p1._passage_of_time()
    assert p1.tiredness == 21
    assert p1.hunger == 21


def test_moods():
    p1 = Pet("Reksio")
    assert p1._mood == "happy"
    for _ in range(7):
        p1._passage_of_time()
    assert p1._mood == "content"
    for _ in range(4):
        p1._passage_of_time()
    assert p1._mood == "annoyed"
    for _ in range(7):
        p1._passage_of_time()
    assert p1._mood == "mad"


def test_talk(capsys):
    p1 = Pet("Reksio")
    p1.talk()
    for _ in range(7):
        p1._passage_of_time()
    p1.talk()
    for _ in range(4):
        p1._passage_of_time()
    p1.talk()
    for _ in range(7):
        p1._passage_of_time()
    p1.talk()
    out, err = capsys.readouterr()
    assert out.strip() == (
        "Reksio is happy\n" "Reksio is content\n" "Reksio is annoyed\n" "Reksio is mad"
    )


def test_eat():
    p1 = Pet("Reksio")
    p1.hunger = 10
    p1.eat()
    assert p1.hunger == 7
    p1.eat(1)
    assert p1.hunger == 7


def test_play():
    p1 = Pet("Reksio")
    p1.tiredness = 10
    p1.play()
    assert p1.tiredness == 7
    p1.play(3)
    assert p1.tiredness == 5


def test_passage_of_time_for_eat_play_talk():
    p1 = Pet("reksio")
    p1.hunger = 10
    p1.tiredness = 10
    assert p1.hunger == 10
    assert p1.tiredness == 10
    p1.eat(0)
    assert p1.hunger == 11
    assert p1.tiredness == 11
    p1.talk()
    assert p1.hunger == 12
    assert p1.tiredness == 12
    p1.play(0)
    assert p1.hunger == 13
    assert p1.tiredness == 13


def test_str():
    p1 = Pet("Reksio")
    assert str(p1) == "Pet's name: Reksio, hunger: 0, tiredness: 0"
