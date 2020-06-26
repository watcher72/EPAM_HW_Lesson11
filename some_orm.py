import json

from typing import List, Dict, Any, Iterator
# from pprint import pprint as pp


def select(*field_names: str) -> callable:
    """
    Create a function for selecting the fields of data in 'query'.

    :param field_names: The list of fields for selection
    :return: The function for selecting the fields
    """
    def inner(data: List[Dict[str, Any]]) -> Iterator:
        return map(
            lambda row: {key: row[key] for key in row if key in field_names},
            data)

    return inner


def field_filter(field_name: str, *values: str) -> callable:
    """
    Create a function for filtering the data in 'query'.

    :param field_name: The name of field for filtering
    :param values: The list of values for this field
    :return: The function
    """
    def inner(data: List[Dict[str, Any]]) -> Iterator:
        return filter(lambda row: row[field_name] in values, data)

    return inner


def query(filepath: str,
          selection: callable,
          *filters: callable
          ) -> List[Dict[str, Any]]:
    """
    Select fields in each row of the 'data', leave only the the fields
    which return 'selection' and filtered them via calls of 'filters'.

    :param filepath: The path to the json-file
    :param selection: The function, which select the fields of interest
    :param filters: The functions for filtering the fields
    :return: The list of filtered records from 'data', including only fields of interest
    """

    with open(filepath, 'r') as f:
        data = json.load(f)

    for function in [selection, *filters]:
        data = function(data)

    return list(data)
