import common

ROCK, PAPER, SCISSORS = 1, 2, 3

opponent_moves = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS
}

strategy_moves = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS
}


def winner(first, second):
    if first == ROCK and second == SCISSORS:
        return 0
    elif first == PAPER and second == ROCK:
        return 0
    elif first == SCISSORS and second == PAPER:
        return 0
    elif second == ROCK and first == SCISSORS:
        return 1
    elif second == PAPER and first == ROCK:
        return 1
    elif second == SCISSORS and first == PAPER:
        return 1

    return None


if __name__ == "__main__":
    for input_file in common.inputs:
        outcome = 0

        for line in common.read_file(input_file):
            move, response = line.split(" ")

            opponent = opponent_moves[move]
            strategy = strategy_moves[response]
            victor = winner(opponent, strategy)

            if victor == 0:
                result = 0
            elif victor == 1:
                result = 6
            else:
                result = 3

            outcome += (result + strategy)

        print(outcome)
