from copy import deepcopy
import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class Instruction:
    count: int
    from_: int
    to: int


Stacks = list[list[str]]
ParsedInput = tuple[Stacks, list[Instruction]]

STACK_ITEM_EXPRESSION = re.compile(r"(?:   |\[([A-Z])\])(?: |$)")
MOVEMENT_INSTRUCTION_EXPRESSION = re.compile(
    r"move (?P<count>\d+) from (?P<from>\d+) to (?P<to>\d+)")


def parse_stacks(stack_description: str) -> Stacks:
    stack_lines = stack_description.splitlines()
    stack_count = len(STACK_ITEM_EXPRESSION.findall(stack_lines[0]))
    stacks: ParsedInput = [list() for _ in range(stack_count)]

    for line in stack_lines:
        items = STACK_ITEM_EXPRESSION.findall(line)
        for index, item in enumerate(items):
            if item == "":
                continue
            stacks[index].insert(0, item)

    return stacks


def parse_movement_instructions(
        movement_instructions: str) -> list[Instruction]:
    instructions = []
    for line in movement_instructions.splitlines():
        instruction = MOVEMENT_INSTRUCTION_EXPRESSION.match(line)
        assert instruction is not None, \
            f"Couldn't parse movement instruction fron line \"{line}\""
        match_ = instruction.groupdict()
        instructions.append(
            Instruction(count=int(match_["count"]),
                        from_=int(match_["from"]),
                        to=int(match_["to"])))

    return instructions


def parse_day_input(day_input: str) -> ParsedInput:
    stack_description, movement_instructions = day_input.split("\n\n",
                                                               maxsplit=1)

    return (parse_stacks(stack_description),
            parse_movement_instructions(movement_instructions))


def move_stacks_part_1(stacks: Stacks,
                       movement_instructions: list[Instruction]) -> Stacks:
    moved_stacks = deepcopy(stacks)
    for instruction in movement_instructions:
        to_index = instruction.to - 1
        from_index = instruction.from_ - 1

        for _ in range(instruction.count):
            moved_stacks[to_index].append(moved_stacks[from_index].pop())

    return moved_stacks


def solve_part_1(moved_stacks: Stacks,
                 movement_instructions: list[Instruction]) -> int:
    moved_stacks = move_stacks_part_1(moved_stacks, movement_instructions)
    return "".join(stack[-1] for stack in moved_stacks)


def move_stacks_part_2(stacks: Stacks,
                       movement_instructions: list[Instruction]) -> Stacks:
    moved_stacks = deepcopy(stacks)
    for instruction in movement_instructions:
        to_index = instruction.to - 1
        from_index = instruction.from_ - 1

        moved_stacks[to_index] += \
            moved_stacks[from_index][-(instruction.count)::1]
        moved_stacks[from_index] = \
            moved_stacks[from_index][:-instruction.count]

    return moved_stacks


def solve_part_2(moved_stacks: Stacks,
                 movement_instructions: list[Instruction]) -> int:
    moved_stacks = move_stacks_part_2(moved_stacks, movement_instructions)
    return "".join(stack[-1] for stack in moved_stacks)


def main() -> None:
    with open("input.txt") as f:
        day_input = f.read().rstrip("\n")

    stacks, movement_instructions = parse_day_input(day_input)
    print(f"Part 1: {solve_part_1(stacks, movement_instructions)}")
    print(f"Part 2: {solve_part_2(stacks, movement_instructions)}")


if __name__ == "__main__":
    main()
