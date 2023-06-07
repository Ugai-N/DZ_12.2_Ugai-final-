import pytest
from utils.dicts import get_val


@pytest.mark.parametrize('collection, key, default, expected', [
    ({'Helen': 1234, 'John': 4321, 'Chris': 777}, 'Chris', 'git', 777),
    ({'Helen': 1234, 'John': 4321, 'Chris': 777}, 'chris', 'git', 777),
    ({'Helen': 1234, 'John': 4321, 'Chris': 777}, 'abrakadabra', 'git', 'git'),
    ({}, 'chris', 'git', 'git'),
    ({}, 'chris', 'blabla', 'blabla'),
])
def test_get_val(collection, key, default, expected):
    assert get_val(collection, key, default) == expected
