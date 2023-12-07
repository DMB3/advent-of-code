import common

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def is_game_possible(sets):
    for a_set in [p.strip() for p in sets.split(";")]:
        cubes = [p.strip() for p in a_set.split(",")]
        for cube in cubes:
            number, colour = [p.strip() for p in cube.split(" ")]

            if int(number) > LIMITS[colour]:
                return False

    return True


if __name__ == "__main__":
    for input_file in common.inputs:
        result = 0

        for line in common.read_file(input_file):
            game, all_sets = [p.strip() for p in line.split(":")]

            if is_game_possible(all_sets):
                result += int(game.split(" ")[1])

        print(input_file, result)
