import common


def fewer_than(x, y, grid, limit=4):
    coordinates_to_check = [
        (y, x - 1),
        (y, x + 1),
        (y - 1, x - 1),
        (y - 1, x + 1),
        (y - 1, x),
        (y + 1, x - 1),
        (y + 1, x + 1),
        (y + 1, x),
    ]
    cnt = 0

    for ny, nx in coordinates_to_check:
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] == "@":
            cnt += 1
            if cnt >= limit:
                return False

    return cnt < 4


if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        grid = []
        for line in common.read_file(input_file):
            grid.append(line)

        result = 0
        for y, row in enumerate(grid):
            for x, item in enumerate(grid[y]):
                if item == "@":
                    if fewer_than(x, y, grid):
                        result += 1

        print(result)
