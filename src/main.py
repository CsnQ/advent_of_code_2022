from pathlib import Path

from src import day_1_solver, day_2_solver
from src.utils import text_parser


def run_puzzles():
    print("**********************")
    print("Day 1")
    answer_day_1()
    print("**********************")

    print("**********************")
    print("Day 2")
    answer_day_2()
    print("**********************")


def answer_day_1():
    input_path = Path().cwd() / 'src' / 'input' / 'day_1.txt'
    data = text_parser.read_list_from_file_as_int_list(input_path)
    print(day_1_solver.part_1(data))
    print(day_1_solver.part_2(data))


def answer_day_2():
    input_path = Path().cwd() / 'src' / 'input' / 'day_2.txt'
    data = text_parser.read_list_from_file_as_string_list(input_path)
    print(day_2_solver.part_1(data))
    print(day_2_solver.part_2(data))


if __name__ == '__main__':
    run_puzzles()
