from dataclasses import dataclass


@dataclass
class Assignment:
    start: int
    end: int


ParsedInput = list[tuple[Assignment, Assignment]]


def parse_day_input(day_input: str) -> ParsedInput:

    def parse_line(line: str) -> tuple[Assignment, Assignment]:
        assignments = [assignment.split("-") for assignment in line.split(",")]
        assert len(assignments) == 2, \
            f"Found more than 2 assingments in line {line}"
        return tuple(
            Assignment(int(start), int(end)) for (start, end) in assignments)

    return [parse_line(line) for line in day_input.splitlines()]


def assignments_fully_overlap(first: Assignment, second: Assignment) -> bool:
    return (first.start <= second.start <= second.end <= first.end) \
        or (second.start <= first.start <= first.end <= second.end)


def solve_part_1(parsed_input: ParsedInput) -> int:
    return sum(
        1 for first_assignment, second_assignment in parsed_input
        if assignments_fully_overlap(first_assignment, second_assignment))


def assignments_have_overlap(first: Assignment, second: Assignment) -> bool:
    return (first.start <= second.end <= first.end) \
        or (second.start <= first.end <= second.end)


def solve_part_2(parsed_input: ParsedInput) -> int:
    return sum(
        1 for first_assignment, second_assignment in parsed_input
        if assignments_have_overlap(first_assignment, second_assignment))


def main() -> None:
    with open("input.txt") as f:
        day_input = f.read().rstrip("\n")

    parsed_input = parse_day_input(day_input)
    print(f"Part 1: {solve_part_1(parsed_input)}")
    print(f"Part 2: {solve_part_2(parsed_input)}")


if __name__ == "__main__":
    main()
