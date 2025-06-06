"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_max, daily_min
# An alternative way to do this rather than listing all functions would be 
# to just do 'import inflammation.models'
# To then call these you would need to do r.g. 'inflammation.models.daily_mean'

@pytest.mark.parametrize(
        "test, expected",
        [
            ([ [0,0], [0,0], [0,0] ], [0,0] ),
            ([ [1,2], [3,4], [5,6] ], [3,4] ), 
        ]
)
def test_daily_mean(test, expected):
    """Test mean function works for array of zeros and positive integers."""
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


# def test_daily_mean_zeros():
#     """Test that mean function works for an array of zeros."""
    
#     test_input = np.array([[0, 0],
#                            [0, 0],
#                            [0, 0]])
#     test_result = np.array([0, 0])

#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)


# def test_daily_mean_integers():
#     """Test that mean function works for an array of positive integers."""

#     test_input = np.array([[1, 2],
#                            [3, 4],
#                            [5, 6]])
#     test_result = np.array([3, 4])

#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_min_integers():
    """Test that min function works for an array of positive integers."""

    test_input = np.array([[2, 2],
                           [6, 4],
                           [6, 8]])
    test_result = np.array([2, 2])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)


def test_daily_max_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_min_string():
    """Test for TypeError when passing strings"""

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'],['General', 'Kenobi']])