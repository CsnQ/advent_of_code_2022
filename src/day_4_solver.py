class ProcessedTaskPair:
    def __init__(self, task_pair):
        self.task_pair = task_pair
        self.tasks = task_pair.split(',')
        self.task_a = self.tasks[0].split('-')
        self.task_b = self.tasks[1].split('-')
        self.a_min = int(self.task_a[0])
        self.a_max = int(self.task_a[1])
        self.b_min = int(self.task_b[0])
        self.b_max = int(self.task_b[1])


def part_1(task_superset: list[str]) -> int:
    overlap_counter = 0
    for task_pair in task_superset:
        tasks = ProcessedTaskPair(task_pair)

        if tasks.a_min == tasks.b_min and tasks.a_max == tasks.b_max:
            overlap_counter += 1
            continue

        if tasks.a_min <= tasks.b_min and tasks.a_max >= tasks.b_max:
            overlap_counter += 1
            continue

        if tasks.a_min >= tasks.b_min and tasks.a_max <= tasks.b_max:
            overlap_counter += 1
            continue

    return overlap_counter


def part_2(task_superset: list[str]) -> int:
    overlap_counter = 0
    for task_pair in task_superset:
        tasks = ProcessedTaskPair(task_pair)

        if tasks.a_max >= tasks.b_min and tasks.b_max >= tasks.a_min:
            overlap_counter += 1

    return overlap_counter
