import common


def carve_path(cave, path):
    for index in range(len(path) - 1):
        one, two = path[index], path[index + 1]

        one_x, one_y = one
        two_x, two_y = two
        for x in range(min(one_x, two_x), max(one_x, two_x) + 1):
            for y in range(min(one_y, two_y), max(one_y, two_y) + 1):
                cave.add(x, y, common.CaveRock)


if __name__ == "__main__":
    for input_file in common.inputs:
        sand_x, sand_y = 500, 0

        mini_x, mini_y = 500, 0
        maxi_x, maxi_y = 500, 0

        full_paths = []

        for line in common.read_file(input_file):
            full_path = []
            paths = line.split("->")

            for path in paths:
                path_x, path_y = path.split(",")
                path_x, path_y = int(path_x), int(path_y)
                full_path.append((path_x, path_y))

                mini_x, mini_y = min(mini_x, path_x), min(mini_y, path_y)
                maxi_x, maxi_y = max(maxi_x, path_x), max(maxi_y, path_y)

            full_paths.append(full_path)

        cave = common.Cave()
        for x in range(mini_x, maxi_x + 1):
            for y in range(mini_y, maxi_y + 1):
                cave.add(x, y, common.CaveAir)

        for path in full_paths:
            carve_path(cave, path)

        cave.add(sand_x, sand_y, common.CaveSandGenerator)

        times = 0
        try:
            while True:
                cave.sand_generator.generate()
                times += 1
        except common.IntoTheAbyss:
            print(cave)
            print(times)
