def part_1(task_superset: list[str]) -> int:
    overlap_counter = 0
    for task_pair in task_superset:
        tasks = task_pair.split(',')
        task_a = tasks[0].split('-')
        task_b = tasks[1].split('-')

        task_a_min = int(task_a[0])
        task_a_max = int(task_a[1])
        task_b_min = int(task_b[0])
        task_b_max = int(task_b[1])

        if task_a_min == task_b_min and task_a_max == task_b_max:
            overlap_counter += 1
            continue

        if task_a_min <= task_b_min and task_a_max >= task_b_max:
            overlap_counter += 1
            continue

        if task_a_min >= task_b_min and task_a_max <= task_b_max:
            overlap_counter += 1
            continue

    return overlap_counter


def part_2(task_superset: list[str]) -> int:
    overlap_counter = 0
    for task_pair in task_superset:
        tasks = task_pair.split(',')
        task_a = tasks[0].split('-')
        task_b = tasks[1].split('-')

        task_a_min = int(task_a[0])
        task_a_max = int(task_a[1])
        task_b_min = int(task_b[0])
        task_b_max = int(task_b[1])

        if task_a_max >= task_b_min and task_b_max >= task_a_min:
            overlap_counter += 1

    return overlap_counter
