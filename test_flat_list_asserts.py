from flat_list import flat_list


def test_empty_list():
    actual_1 = flat_list([])
    actual_2 = flat_list([[], []])
    expected = []
    assert actual_1 == expected, f'{actual_1} != {expected}'
    assert actual_2 == expected, f'{actual_2} != {expected}'


def test_nested_list():
    actual = flat_list([[1, 2, [3, 4], 5, [[6, [7]], 8], 9]])
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert actual == expected, f'{actual} != {expected}'


def test_argument_is_not_list():
    try:
        flat_list(5)
    except TypeError as e:
        assert e.args[0] == 'Argument must be a list', 'Wrong exception'
        return


if __name__ == '__main__':
    test_empty_list()
    test_nested_list()
    test_argument_is_not_list()
    print('All test passed!')
