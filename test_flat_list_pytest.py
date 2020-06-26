import pytest

from flat_list import flat_list


def test_empty_list():
    actual_1 = flat_list([])
    actual_2 = flat_list([[], []])
    assert actual_1 == []
    assert actual_2 == []


def test_nested_list():
    actual = flat_list([[1, 2, [3, 4], 5, [[6, [7]], 8], 9]])
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert actual == expected


def test_argument_is_not_list():
    with pytest.raises(TypeError) as e:
        flat_list(5)
    assert str(e.value) == 'Argument must be a list', "Wrong exception!"
