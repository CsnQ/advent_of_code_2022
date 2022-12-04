import pytest

from src.day_4_solver import part_1, part_2


@pytest.fixture
def example_input():
    return ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']


class TestPart1:
    def test_returns_1_when_list_a_contains_all_from_list_b(self):
        test_input = ['2-8, 3-7']
        expected_result = 1
        actual_result = part_1(test_input)
        assert actual_result == expected_result

    def test_returns_1_when_list_b_contains_all_from_list_a(self):
        test_input = ['3-7, 2-8']
        expected_result = 1
        actual_result = part_1(test_input)
        assert actual_result == expected_result

    def test_returns_1_when_common_min_val_in_list(self):
        test_input = ['3-7, 3-8']
        expected_result = 1
        actual_result = part_1(test_input)
        assert actual_result == expected_result

    def test_returns_1_when_common_max_val_in_list(self):
        test_input = ['3-7, 2-7']
        expected_result = 1
        actual_result = part_1(test_input)
        assert actual_result == expected_result

    def test_returns_1_when_vals_are_same(self):
        test_input = ['2-8, 2-8']
        expected_result = 1
        actual_result = part_1(test_input)
        assert actual_result == expected_result

    def test_returns_2_with_test_input(self, example_input):
        expected_result = 2
        actual_result = part_1(example_input)
        assert actual_result == expected_result

class TestPart2:
    def test_returns_1_with_example_data(self):
        test_input = ['5-7,7-9']
        expected_result = 1
        actual_result = part_2(test_input)
        assert actual_result == expected_result

    def test_returns_1_with_example_data_variation_1(self):
        test_input = ['2-8,3-7']
        expected_result = 1
        actual_result = part_2(test_input)
        assert actual_result == expected_result

    def test_returns_1_with_example_data_variation_2(self):
        test_input = ['6-6,4-6']
        expected_result = 1
        actual_result = part_2(test_input)
        assert actual_result == expected_result

    def test_returns_1_with_example_data_variation_3(self):
        test_input = ['2-6,4-8']
        expected_result = 1
        actual_result = part_2(test_input)
        assert actual_result == expected_result

    def test_returns_4_with_test_input(self, example_input):
        expected_result = 4
        actual_result = part_2(example_input)
        assert actual_result == expected_result
