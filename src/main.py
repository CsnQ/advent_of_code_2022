from pathlib import Path

from src.day_1.day_1_solver import Day1
from src.utils.text_parser import TextParser


def run_puzzles():
    print("**********************")
    print("Day 1")
    answer_day_1()
    print("**********************")


def answer_day_1():
    input_path = Path().cwd() / 'src' / 'input' / 'day_1.txt'
    data = TextParser().read_list_from_file_as_int_list(input_path)
    print(Day1.part_1(data))
    print(Day1.part_2(data))


if __name__ == '__main__':
    run_puzzles()
