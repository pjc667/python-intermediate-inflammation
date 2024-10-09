"""Tests for statistics functions within the Model layer."""
import os
import pytest
import numpy as np
import numpy.testing as npt
from inflammation.models import load_json
from inflammation.models import daily_mean
from inflammation.models import daily_min

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])

def test_daily_mean(test,expected):
    """ test means for zeros and positive integers"""

    npt.assert_array_equal(daily_mean(np.array(test)),np.array(expected))


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    
    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_min_zeros():
    """Test daily_min function works for zeros"""
    
    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # still using Numpy testing functions
    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_load_from_json(tmpdir):
    
    example_path = os.path.join(tmpdir, 'example.json')
    with open(example_path, 'w') as temp_json_file:
        temp_json_file.write('[{"observations":[1, 2, 3]},{"observations":[4, 5, 6]}]')
    result = load_json(example_path)
    npt.assert_array_equal(result, [[1, 2, 3], [4, 5, 6]])
