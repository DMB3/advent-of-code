import common

ORIENTATION = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

RIGHT_TURN = {
    "^": ">",
    "v": "<",
    "<": "^",
    ">": "v",
}


class MapObject(object):
    def __init__(self, the_map, row, column, visited=False):
        self.__map = the_map
        self.__row = row
        self.__column = column
        self.__visited = visited

    def visit(self):
        self.__visited = True

    @property
    def visited(self):
        return self.__visited

    @property
    def has_guard(self):
        return False

    @property
    def coordinates_string(self):
        return f"row:${self.__row},column:${self.__column}"

    @property
    def coordinates(self):
        return self.__row, self.__column

    @property
    def the_map(self):
        return self.__map

    def walk(self):
        raise ValueError("walk() should only be used on the guard object")


class Obstacle(MapObject):
    def __init__(self, the_map, row, column):
        MapObject.__init__(self, the_map, row, column)

    def __repr__(self):
        return "#"


class Empty(MapObject):
    def __init__(self, the_map, row, column, has_guard=False, guard_orientation=None):
        MapObject.__init__(self, the_map, row, column)
        self.__has_guard = has_guard
        self.__guard_orientation = guard_orientation

        if self.__has_guard:
            self.__visited = True

    @property
    def has_guard(self):
        return self.__has_guard

    def walk(self):
        if not self.__has_guard:
            self.the_map.walk()
        else:
            coordinates = ORIENTATION[self.__guard_orientation]

            self_row, self_column = self.coordinates
            target_row = self_row + coordinates[0]
            target_column = self_column + coordinates[1]

            if self.the_map.obstacle_at(target_row, target_column):
                self.__guard_orientation = RIGHT_TURN[self.__guard_orientation]
            else:
                self.the_map.set_guard(target_row, target_column, self.__guard_orientation)

    def clear_guard(self):
        self.__has_guard = False
        self.__guard_orientation = None

    def set_guard(self, guard_orientation):
        self.__has_guard = True
        self.__guard_orientation = guard_orientation

    def __repr__(self):
        return "." if not self.visited else "X"


def object_from_char(the_map, char, row, column):
    if char == ".":
        return Empty(the_map, row, column)
    elif char == "#":
        return Obstacle(the_map, row, column)
    elif char in ("^", "v", "<", ">"):
        return Empty(the_map, row, column, has_guard=True, guard_orientation=char)
    else:
        raise ValueError("Unknown object :'(")


class PuzzleMap(object):
    def __init__(self):
        self.__contents = {}
        self.__guard = None

    def visit(self, row, column):
        self.__contents[row][column].visit()

    @property
    def visited_count(self):
        count = 0

        for row in self.__contents:
            for column in self.__contents[row]:
                if self.__contents[row][column].visited:
                    count += 1

        return count

    def __in_bounds(self, row, column):
        row_in_bounds = 0 <= row < len(self.__contents)
        return row_in_bounds and 0 <= column < len(self.__contents[row])

    def obstacle_at(self, row, column):
        if not self.__in_bounds(row, column):
            return False

        return isinstance(self.__contents[row][column], Obstacle)

    @property
    def guard(self):
        if self.__guard is not None:
            return self.__guard

        for line in self.__contents:
            for row in self.__contents[line]:
                if self.__contents[line][row].has_guard:
                    self.__guard = self.__contents[line][row]
                    return self.__guard

    def set_guard(self, row, column, orientation):
        self.guard.clear_guard()
        if self.__in_bounds(row, column):
            self.__contents[row][column].set_guard(orientation)
            self.visit(row, column)
        self.__guard = None

    def walk(self):
        self.guard.walk()

    def add(self, row, column, obj):
        if row not in self.__contents:
            self.__contents[row] = {}
        self.__contents[row][column] = obj

        if obj.has_guard:
            self.visit(row, column)

    @property
    def is_guard_in_bounds(self):
        if self.guard is None:
            return False

        guard_row, guard_column = self.guard.coordinates
        return self.__in_bounds(guard_row, guard_column)

    def __repr__(self):
        map_str = ""

        for y in range(len(self.__contents)):
            line_str = ""
            for x in range(len(self.__contents[y])):
                line_str = f"{line_str}{self.__contents[y][x]}"
            map_str = f"{map_str}{line_str}\n"

        return map_str.strip()


if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)

        map_layout = PuzzleMap()
        for row, line in enumerate(common.read_file(input_file)):
            for column, char in enumerate(line):
                map_layout.add(row, column, object_from_char(map_layout, char, row, column))

        while map_layout.is_guard_in_bounds:
            map_layout.walk()

        print(map_layout.visited_count)
