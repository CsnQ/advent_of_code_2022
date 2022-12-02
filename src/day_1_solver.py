def part_1(calorie_list: list[list[int]]) -> int:
    total_cals_per_elf = [sum(x)for x in calorie_list]
    return max(total_cals_per_elf)


def part_2(calorie_list: list[list[int]]) -> int:
    total_cals_per_elf = [sum(x)for x in calorie_list]
    total_cals_per_elf.sort(reverse=True)
    return sum(total_cals_per_elf[:3])
