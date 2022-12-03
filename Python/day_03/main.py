from functools import reduce
from typing import Iterable, Iterator

BADGE_GROUP_SIZE = 3


def find_shared_item(rucksack_row: str) -> str:
    assert len(rucksack_row) % 2 == 0, \
        f"Rucksack row is of odd length - '{rucksack_row}'"
    half_row_length = len(rucksack_row) // 2
    first_rucksack = set(rucksack_row[:half_row_length])
    second_rucksack = set(rucksack_row[half_row_length:])
    shared_item = first_rucksack.intersection(second_rucksack)
    assert len(shared_item) == 1, \
        "Found more than one shared item between rucksacks "\
        f"'{first_rucksack}' and '{second_rucksack}'"
    return shared_item.pop()


def prioritize_item(item: str) -> int:
    assert len(item) == 1, "Got item with length != 1"
    priority = ord(item.lower()[0]) - 96
    if item.isupper():
        return priority + 26
    return priority


def groups(iterable: Iterable, n: int) -> Iterator[tuple]:
    return zip(*([iter(iterable)] * n), strict=True)


def find_group_badge(group_lines: Iterable[str]) -> str:
    group_items = [set(line) for line in group_lines]
    badge = reduce(set.intersection, group_items)
    assert len(badge) == 1, \
        f"Found more than one possible badge for group {group_items}"
    return badge.pop()


def solve_day_3_part_1(day_input: str) -> int:
    return sum(
        prioritize_item(find_shared_item(row))
        for row in day_input.splitlines())


def solve_day_3_part_2(day_input: str) -> int:
    return sum(
        prioritize_item(find_group_badge(elf_group_lines)) for elf_group_lines
        in groups(day_input.splitlines(), BADGE_GROUP_SIZE))


def main() -> None:
    with open("input.txt") as f:
        day_input = f.read().rstrip("\n")

    print(f"Part 1: {solve_day_3_part_1(day_input)}")
    print(f"Part 2: {solve_day_3_part_2(day_input)}")


if __name__ == "__main__":
    main()
