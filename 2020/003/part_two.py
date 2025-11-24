import common
import math

if __name__ == "__main__":
    for input_file in common.inputs:
        parts = []
        for line in common.read_file(input_file):
            parts.append(line)

        results = []
        for increase_x, increase_y in [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2),
        ]:
            current_x, current_y = 0, 0
            trees = 0
            while current_y <= len(parts) - 1:
                current_spot = parts[current_y][current_x]
                if current_spot == '#':
                    trees += 1

                current_x, current_y = (current_x + increase_x) % len(parts[current_y]), current_y + increase_y

            results.append(trees)

        print(input_file, results, math.prod(results))
