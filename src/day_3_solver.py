from typing import List

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def part_1(rucksack_contents: List[str]) -> int:
    total = 0
    for content in rucksack_contents:
        half = int(len(content) / 2)
        first_compartment = set(content[:half])
        second_compartment = set(content[half:])
        common_item = list(first_compartment.intersection(second_compartment))[0]
        total = get_running_total(common_item, total)

    return total


def part_2(rucksack_contents: List[str]) -> int:
    total = 0
    groupings = get_rucksack_groupings(rucksack_contents)
    for group in groupings:
        group_1_set = set(group[0])
        group_2_set = set(group[1])
        group_3_set = set(group[2])
        intersection_of_1_and_2 = group_1_set.intersection(group_2_set)
        common_item = list(group_3_set.intersection(intersection_of_1_and_2))[0]
        total = get_running_total(common_item, total)

    return total


def get_running_total(common_item: str, current_total: int) -> int:
    letter_value = letters.index(common_item) + 1
    total = current_total + letter_value
    return total


def get_rucksack_groupings(rucksack_contents: List[str]) -> List[List[str]]:
    grouping = 3
    groupings = []
    for i in range(0, len(rucksack_contents), grouping):
        group = yield rucksack_contents[i:i + grouping]
        groupings.append(group)
    return groupings
