from typing import List


class Day1:
    @staticmethod
    def part_1(calorie_list: List[List[int]]) -> int:
        total_cals_per_elf = [sum(x)for x in calorie_list]
        return max(total_cals_per_elf)

    @staticmethod
    def part_2(calorie_list: List[List[int]]) -> int:
        total_cals_per_elf = [sum(x)for x in calorie_list]
        total_cals_per_elf.sort(reverse=True)
        return sum(total_cals_per_elf[:3])
