
import pytest as pytest

from src.day_1 import day_1_solver


class TestDay1Part1:

    @pytest.fixture
    def test_input_truncated(self) -> list[list[int]]:
        return [[1000, 2000, 3000]]

    @pytest.fixture
    def test_input(self) -> list[list[int]]:
        return [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]

    def test_part_1_returns_6000(self, test_input_truncated):
        expected_result = 6000
        result = day_1_solver.part_1(test_input_truncated)
        assert result == expected_result

    def test_part_1_returns_24000(self, test_input):
        expected_result = 24000
        result = day_1_solver.part_1(test_input)
        assert result == expected_result

    def test_part_2_returns_45000(self, test_input):
        expected_result = 45000
        result = day_1_solver.part_2(test_input)
        assert result == expected_result

