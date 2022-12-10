from enum import Enum
from dataclasses import dataclass
from functools import reduce
from typing import Generator


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


@dataclass
class Coordinates:
    row: int
    column: int


TreeGrid = list[list[int]]
ALL_DIRECTIONS = (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT)


def parse_day_input(day_input: str) -> TreeGrid:
    def parse_line(line: str) -> list[int]:
        return list(map(int, line.rstrip("\n")))

    grid = [parse_line(line) for line in day_input.splitlines()]
    assert (
        len(set(len(line) for line in grid)) == 1
    ), "Rows have mismatching columns in grid"
    return grid


def iterate_trees(grid: TreeGrid) -> Generator[tuple[int, Coordinates], None, None]:
    for row_index, column in enumerate(grid):
        for column_index, height in enumerate(column):
            yield Coordinates(row_index, column_index)


def iterate_trees_outwards(
    grid: TreeGrid, coordinates: Coordinates, direction: Direction
) -> Generator[int, None, None]:
    row, column = coordinates.row, coordinates.column

    match direction:
        case Direction.UP:
            return (grid[x][column] for x in reversed(range(0, row)))
        case Direction.DOWN:
            return (grid[x][column] for x in range(row + 1, len(grid)))
        case Direction.LEFT:
            return (grid[row][x] for x in reversed(range(0, column)))
        case Direction.RIGHT:
            return (grid[row][x] for x in range(column + 1, len(grid[0])))
        case other_direction:
            raise ValueError(f"Invalid direction: {other_direction}")


def tree_visible_from_outside_grid(
    grid: TreeGrid, coordinates: Coordinates, direction: Direction
) -> bool:
    given_tree_height = grid[coordinates.row][coordinates.column]
    return not any(
        tree_height >= given_tree_height
        for tree_height in iterate_trees_outwards(grid, coordinates, direction)
    )


def solve_part_1(grid: TreeGrid):
    return sum(
        1
        for coordinates in iterate_trees(grid)
        if any(
            tree_visible_from_outside_grid(grid, coordinates, direction)
            for direction in ALL_DIRECTIONS
        )
    )


def get_viewing_distance(
    grid: TreeGrid, coordinates: Coordinates, direction: Direction
) -> int:
    given_tree_height = grid[coordinates.row][coordinates.column]
    view_distance = 0
    for tree_height in iterate_trees_outwards(grid, coordinates, direction):
        view_distance += 1
        if tree_height >= given_tree_height:
            break

    return view_distance


def get_scenic_score(grid: TreeGrid, coordinates: Coordinates) -> int:
    return reduce(
        lambda sum, value: sum * value,
        (
            get_viewing_distance(grid, coordinates, direction)
            for direction in ALL_DIRECTIONS
        ),
        1,
    )


def solve_part_2(grid: TreeGrid):
    return max(
        get_scenic_score(grid, coordinates) for coordinates in iterate_trees(grid)
    )


def main() -> None:
    with open("input.txt") as f:
        day_input = f.read().rstrip("\n")

    tree_grid = parse_day_input(day_input)
    print(f"Part 1: {solve_part_1(tree_grid)}")
    print(f"Part 2: {solve_part_2(tree_grid)}")


if __name__ == "__main__":
    main()
