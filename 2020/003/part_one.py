import common

if __name__ == "__main__":
    for input_file in common.inputs:
        parts = []
        for line in common.read_file(input_file):
            parts.append(line)

        current_x, current_y = 0, 0
        trees = 0
        while current_y <= len(parts) - 1:
            current_spot = parts[current_y][current_x]
            if current_spot == '#':
                trees += 1

            current_x, current_y = (current_x + 3) % len(parts[current_y]), current_y + 1

        print(input_file, trees)
