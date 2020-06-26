import json
import os
import pytest

from some_orm import query, select, field_filter


@pytest.fixture(scope='module')
def prepare_data():
    friends = [
        {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'age': 28},
        {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'age': 22},
        {'name': 'Роберт', 'gender': 'Мужской', 'sport': 'Баскетбол', 'age': 25},
        {'name': 'Амалия', 'gender': 'Женский', 'sport': 'Теннис', 'age': 31},
        {'name': 'Роберт', 'gender': 'Мужской', 'sport': 'Хоккей', 'age': 20},
        {'name': 'Алекс', 'gender': 'Мужской', 'sport': 'Волейбол', 'age': 35},
        {'name': 'Крис', 'gender': 'Мужской', 'sport': 'Теннис', 'age': 27}
    ]
    with open('data.json', 'w') as f:
        json.dump(friends, f)

    yield 'data.json'

    os.remove('data.json')


def test_some_orm_positive(prepare_data):
    actual = query(
        prepare_data,
        select('name', 'gender', 'sport'),
        field_filter('sport', 'Баскетбол', 'Волейбол'),
        field_filter('gender', 'Мужской'),
    )
    expected = [
        {'gender': 'Мужской', 'name': 'Сэм', 'sport': 'Баскетбол'},
        {'gender': 'Мужской', 'name': 'Роберт', 'sport': 'Баскетбол'},
        {'gender': 'Мужской', 'name': 'Алекс', 'sport': 'Волейбол'}
    ]
    assert actual == expected


def test_nothing_found_positive(prepare_data):
    actual = query(
        prepare_data,
        select('name', 'gender', 'sport'),
        field_filter('sport', 'Хоккей'),
        field_filter('gender', 'Женский'),
    )
    assert actual == []


def test_unknown_field(prepare_data):
    with pytest.raises(Exception) as e_info:
        query(
            prepare_data,
            select('name', 'surname', 'sport'),
            field_filter('sport', 'Хоккей'),
            field_filter('gender', 'Женский'),
        )
    assert 'KeyError' in str(e_info)
