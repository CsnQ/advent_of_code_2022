import pytest

from src.day_3_solver import part_1, part_2


@pytest.fixture
def input():
    return ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']


@pytest.fixture
def truncated_input():
    return ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg']


def test_part_1_returns_157(input):
    expected_result = 157
    actual_result = part_1(input)
    assert actual_result == expected_result


def test_part_2_returns_18_with_truncated_input(truncated_input):
    expected_result = 18
    actual_result = part_2(truncated_input)
    assert actual_result == expected_result


def test_part_2_returns_70_with_input(input):
    expected_result = 70
    actual_result = part_2(input)
    assert actual_result == expected_result
