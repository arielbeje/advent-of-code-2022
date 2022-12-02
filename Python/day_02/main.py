with open("input.txt") as f:
    day_input = f.read().rstrip("\n")

EQUALITY_MATRIX = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

# Keys: Opponent, Values: Us
WIN_MATRIX = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}

POINTS_AWARDED = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def score_round(opponents_play: str, our_play: str) -> int:
    our_play_points = POINTS_AWARDED[our_play]

    if WIN_MATRIX[opponents_play] == our_play:
        return our_play_points + 6

    if EQUALITY_MATRIX[opponents_play] == our_play:
        return our_play_points + 3

    return our_play_points


print(sum(score_round(*row.split(" ")) for row in day_input.splitlines()))
