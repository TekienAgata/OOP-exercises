import pytest

from L1Ex5 import Matrix


def test_matrix():
    m1 = Matrix(2, 3, 8)
    assert m1._matrix == [[8, 8, 8], [8, 8, 8]]


def test_size():
    m1 = Matrix(2, 4, 9)
    assert m1.size() == (2, 4)


def test_check_index_too_high():
    m1 = Matrix(6, 2, 0)
    with pytest.raises(IndexError) as err:
        m1._check_index(3, 5)
    assert str(err.value) == "Index outside matrix"


def test_check_index_below_zero():
    m1 = Matrix(4, 12, 1)
    with pytest.raises(IndexError) as err:
        m1._check_index(-5, 12)
    assert str(err.value) == "Index outside matrix"


def test_get_cell_correct():
    m1 = Matrix(5, 5, 5)
    assert m1.get_cell(0, 0) == 5


def test_get_cell_outside():
    m1 = Matrix(5, 5, 5)
    with pytest.raises(IndexError) as err:
        m1.get_cell(-1, 0)
    assert str(err.value) == "Index outside matrix"


def test_set_cell_correct():
    m1 = Matrix(6, 6, 6)
    m1.set_cell(1, 1, 9)
    assert m1.get_cell(1, 1) == 9
    assert m1._matrix[1][1] == 9


def test_str():
    m1 = Matrix(2, 2, 0)
    assert str(m1) == "0 0\n0 0"
