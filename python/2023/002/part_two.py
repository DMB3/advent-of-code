from functools import reduce

import common


def set_powers(sets):
    limits = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for a_set in [p.strip() for p in sets.split(";")]:
        cubes = [p.strip() for p in a_set.split(",")]
        for cube in cubes:
            number, colour = [p.strip() for p in cube.split(" ")]

            limits[colour] = max(limits[colour], int(number))

    return reduce(lambda x, y: x * y, limits.values())


if __name__ == "__main__":
    for input_file in common.inputs:
        result = 0

        for line in common.read_file(input_file):
            game, all_sets = [p.strip() for p in line.split(":")]

            result += set_powers(all_sets)

        print(input_file, result)
