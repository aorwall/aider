import pytest

from saddle_points import saddle_points

def test_empty_matrix():
    assert saddle_points([[]]) == []

def test_matrix_with_one_element():
    assert saddle_points([[1]]) == []

def test_matrix_with_one_row():
    assert saddle_points([[1, 2, 3]]) == []

def test_matrix_with_one_column():
    assert saddle_points([[1], [2], [3]]) == []

def test_matrix_with_saddle_point():
    assert saddle_points([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [(1, 1)]

def test_matrix_with_multiple_saddle_points():
    assert saddle_points([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == [(1, 1), (2, 2)]

def test_matrix_with_irregular_shape():
    with pytest.raises(ValueError):
        saddle_points([[1, 2, 3], [4, 5, 6], [7, 8]])