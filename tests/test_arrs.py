import pytest
from utils import arrs


@pytest.fixture
def long_coll():
    return [1, 2, 3, 4, 5, 6]


def test_get(long_coll):
    assert arrs.get(long_coll, 1, "test") == 2
    assert arrs.get(long_coll, -1, "test") == "test"
    assert arrs.get(long_coll, 7, "test") == "test"
    assert arrs.get([], 0, "test") == "test"


def test_slice(long_coll):
    assert arrs.my_slice(long_coll, 1, 3) == [2, 3]
    assert arrs.my_slice(long_coll, 1) == [2, 3, 4, 5, 6]
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice(long_coll, -4, 5) == [3, 4, 5]
    assert arrs.my_slice(long_coll, -10, 5) == [1, 2, 3, 4, 5]
