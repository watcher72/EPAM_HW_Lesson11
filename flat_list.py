"""
The function 'flat_list' make flat list
from the given any nesting level list.
"""


def flat_list(arg):
    """

    :param arg: multilevel nested list
    :return: flatten list
    """

    if not isinstance(arg, list):
        raise TypeError('Argument must be a list')

    result = []
    for item in arg:
        result.extend(flat_list(item)) if isinstance(item, list) \
            else result.append(item)
    return result
