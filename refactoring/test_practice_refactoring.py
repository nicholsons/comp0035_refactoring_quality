import json

import pytest

from refactoring.practice_refactoring import DataStats


@pytest.fixture
def test_data():
    return [
        {
            "id": 1,
            "name": "Laith",
            "surname": "Simmons",
            "age": 68,
            "salary": "£27888"
        },
        {
            "id": 2,
            "name": "Mikayla",
            "surname": "Henry",
            "age": 49,
            "salary": "£67137"
        },
        {
            "id": 3,
            "name": "Garth",
            "surname": "Fields",
            "age": 70,
            "salary": "£70472"
        }
    ]


def test_json(test_data):
    ds = DataStats()

    assert ds.s(test_data, 20, 20000) == json.dumps(
        {
            'avg_age': 62,
            'avg_salary': 55165,
            'avg_yearly_increase': 837,
            'max_salary': [{
                "id": 3,
                "name": "Garth",
                "surname": "Fields",
                "age": 70,
                "salary": "£70472"
            }],
            'min_salary': [{
                "id": 1,
                "name": "Laith",
                "surname": "Simmons",
                "age": 68,
                "salary": "£27888"
            }]
        }
    )


def test_s(test_data):
    ds = DataStats()

    assert ds.s(test_data, 20, 20000) == {
        'avg_age': 62,
        'avg_salary': 55165,
        'avg_yearly_increase': 837,
        'max_salary': [{
            "id": 3,
            "name": "Garth",
            "surname": "Fields",
            "age": 70,
            "salary": "£70472"
        }],
        'min_salary': [{
            "id": 1,
            "name": "Laith",
            "surname": "Simmons",
            "age": 68,
            "salary": "£27888"
        }]
    }
