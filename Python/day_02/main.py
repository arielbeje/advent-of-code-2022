with open("input.txt") as f:
    day_input = f.read().rstrip("\n")

WIN_POINTS = 6
TIE_POINTS = 3
LOSS_POINTS = 0

# All of the matrices are just shifts of one another
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

LOSS_MATRIX = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

POINTS_AWARDED = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def score_round_part_1(opponents_play: str, our_play: str) -> int:
    our_play_points = POINTS_AWARDED[our_play]

    if WIN_MATRIX[opponents_play] == our_play:
        return our_play_points + WIN_POINTS

    if EQUALITY_MATRIX[opponents_play] == our_play:
        return our_play_points + TIE_POINTS

    return our_play_points + LOSS_POINTS


def score_round_part_2(opponents_play: str, our_play: str) -> int:
    match our_play :
        case "Z":
            return POINTS_AWARDED[WIN_MATRIX[opponents_play]] + WIN_POINTS

        case "Y":
            return POINTS_AWARDED[EQUALITY_MATRIX[opponents_play]] + TIE_POINTS

        case "X":
            return POINTS_AWARDED[LOSS_MATRIX[opponents_play]] + LOSS_POINTS

    raise ValueError("Invalid move for our_play")

print(sum(score_round_part_2(*row.split(" ")) for row in day_input.splitlines()))
