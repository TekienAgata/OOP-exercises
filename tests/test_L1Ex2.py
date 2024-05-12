from L1Ex2 import Sponge


def test_the_sponge():
    sp1 = Sponge()
    sp2 = Sponge(18)
    assert sp1.hydration == 100
    assert sp2.hydration == 18


def test_wing():
    sp1 = Sponge()
    sp2 = Sponge(18)
    sp1.wring()
    sp2.wring()
    assert sp1.hydration == 80
    assert sp2.hydration == 10


def test_wet():
    sp1 = Sponge()
    sp2 = Sponge(18)
    sp1.wet()
    sp2.wet()
    assert sp1.hydration == 100
    assert sp2.hydration == 100


def test_touch(capsys):
    sp = Sponge()
    sp.touch()
    out, err = capsys.readouterr()
    assert out.strip() == "100"


"""
I could add tests to check if the methods influence each other
"""
