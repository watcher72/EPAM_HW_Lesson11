"""
Make flat list from the given list with any nesting level.

>>> flat_list(1, 2, 3)
Traceback (most recent call last):
  ...
TypeError: flat_list() takes 1 positional argument but 3 were given
"""


def flat_list(arg):
    """

    :param arg: multilevel nested list
    :return: flatten list

    >>> flat_list([])
    []
    >>> flat_list([1, 2, [3, 4], 5, [[6, [7]], 8], 9])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    result = []
    for item in arg:
        result.extend(flat_list(item)) if isinstance(item, list) \
            else result.append(item)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
