import collections
from itertools import islice
from typing import Any, Generator, Iterable

# "the start of a packet is indicated by a sequence of four characters that are all different"
START_OF_PACKET_MARKER_LENGTH = 4
START_OF_MESSAGE_MARKER_LENGTH = 14


# From the itertools docs
def sliding_window(iterable: Iterable[str], n: int) -> Generator[tuple[str], Any, Any]:
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def find_marker(stream: str, marker_length: int) -> int:
    for index, window in enumerate(sliding_window(stream, marker_length)):
        if len(set(window)) == marker_length:
            return index + marker_length
    raise ValueError(f"Couldn't find marker sized {marker_length} in input")


def solve_part_1(day_input: str):
    return find_marker(day_input, START_OF_PACKET_MARKER_LENGTH)


def solve_part_2(day_input: str):
    return find_marker(day_input, START_OF_MESSAGE_MARKER_LENGTH)


def main() -> None:
    with open("input.txt") as f:
        day_input = f.read().rstrip("\n")

    print(f"Part 1: {solve_part_1(day_input)}")
    print(f"Part 2: {solve_part_2(day_input)}")


if __name__ == "__main__":
    main()
