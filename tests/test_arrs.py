from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([], 5, "test") == 'test'
    assert arrs.get([1, 2, 3], 7, "test") == 'test'
    assert arrs.get([1, 2, 3], 7) is None


def test_my_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4], -3, -1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 0, -3) == [1]
    assert arrs.my_slice([1, 2, 3, 4], -3, -3) == []
    assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], -1, -3) == []
