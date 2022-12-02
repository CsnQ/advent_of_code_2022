import pytest

from src.day_2_solver import part_1, part_2


@pytest.fixture
def truncated_test_input():
    return ['A Y']


@pytest.fixture
def test_input():
    return ['A Y', 'B X', 'C Z']


def test_part_1_returns_8_for_one_round(truncated_test_input):
    expected_result = 8
    actual_result = part_1(truncated_test_input)
    assert actual_result == expected_result


def test_part_1_returns_15(test_input):
    expected_result = 15
    actual_result = part_1(test_input)
    assert actual_result == expected_result


def test_part_2_returns_4(truncated_test_input):
    expected_result = 4
    actual_result = part_2(truncated_test_input)
    assert actual_result == expected_result


def test_part_2_returns_12(test_input):
    expected_result = 12
    actual_result = part_2(test_input)
    assert actual_result == expected_result
