import common


def draw_map(my_map, width, height):
    for y in range(height):
        row = ""
        for x in range(width):
            row += chr(my_map[(x, y)])
        print(row)


def find_neighbours(my_map, node):
    x, y = node
    neighbours = []
    height = my_map[(x, y)]

    possibilities = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for possibility in possibilities:
        target_height = my_map.get(possibility, 2e10)
        if target_height <= height or target_height == height + 1:
            neighbours.append(possibility)

    return neighbours


def shortest_path(my_map, start, end):
    seen = []
    queue = [[start]]

    if start == end:
        return []

    while queue:
        current_path = queue.pop(0)
        current_node = current_path[-1]

        if current_node not in seen:
            neighbours = find_neighbours(my_map, current_node)
            for neighbour in neighbours:
                new_path = list(current_path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == end:
                    return new_path

            seen.append(current_node)

    return None


if __name__ == "__main__":
    for input_file in common.inputs:
        my_map = {}
        start_locations = []
        end_location = None

        y = 0
        for line in common.read_file(input_file):
            x = 0
            for c in line:
                if c == "S":
                    start_locations.append((x, y))
                    height = ord("a")
                elif c == "E":
                    end_location = (x, y)
                    height = ord("z")
                else:
                    if c == "a":
                        start_locations.append((x, y))
                    height = ord(c)

                my_map[(x, y)] = height

                x += 1

            y += 1

        shortest = 2e10
        for start_location in start_locations:
            path = shortest_path(my_map, start_location, end_location)
            if path is not None:
                shortest = min(shortest, len(path) - 1)
        print(shortest)
