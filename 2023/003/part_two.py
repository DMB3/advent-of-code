from functools import reduce

import common


def find_to_the_left(line, column):
    digits = ""

    c = column - 1
    while c >= 0:
        character = line[c]

        if character.isdigit():
            digits = character + digits
        else:
            break

        c -= 1

    return digits, c + 1


def find_to_the_right(line, column):
    digits = ""

    c = column + 1
    while c < len(line):
        character = line[c]

        if character.isdigit():
            digits += character
        else:
            break

        c += 1

    return digits, c - 1


def get_adjacent_number(schematic, row, column):
    if row < 0 or column < 0:
        return None, None

    max_row, max_column = len(schematic) - 1, len(schematic[row]) - 1
    if row > max_row or column > max_column:
        return None, None

    character = schematic[row][column]
    if not character.isdigit():
        return None, None

    left_digits, position = find_to_the_left(schematic[row], column)
    right_digits, _ = find_to_the_right(schematic[row], column)
    digits = left_digits + character + right_digits

    return int(digits), position


if __name__ == "__main__":
    for input_file in common.inputs:
        symbol_spots = []
        found_positions = set()

        lines = list(common.read_file(input_file))
        for y, line in enumerate(lines):
            for x, character in enumerate(line):
                if not character.isdigit() and character == "*":
                    symbol_spots.append((y, x))

        result = 0
        for y, x in symbol_spots:
            adjacent_numbers = []
            for adjacency_y, adjacency_x, description in [
                (y, x - 1, "left"),
                (y, x + 1, "right"),
                (y - 1, x, "up"),
                (y + 1, x, "down"),
                (y - 1, x - 1, "up-left"),
                (y - 1, x + 1, "up-right"),
                (y + 1, x - 1, "down-left"),
                (y + 1, x + 1, "down-right"),
            ]:
                number, position = get_adjacent_number(lines, adjacency_y, adjacency_x)
                if number is not None:
                    position = (adjacency_y, position)
                    if position not in found_positions:
                        adjacent_numbers.append(number)
                        found_positions.add(position)

            if len(adjacent_numbers) == 2:
                result += reduce((lambda x, y: x * y), adjacent_numbers)

        print(input_file, result)
