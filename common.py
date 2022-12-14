import os

inputs = [os.path.join("inputs", "example_input.txt"),
          os.path.join("inputs", "real_input.txt")]


def read_file(filename, strip_lines=True):
    with open(filename, "r") as fin:
        for line in fin.readlines():
            if strip_lines:
                line = line.strip()

            yield line


class FilesystemObject(object):
    def __init__(self, filesystem, name, parent):
        self.filesystem = filesystem
        self.name = name
        self.parent = parent

        self.contents = []


class Directory(FilesystemObject):
    def __init__(self, filesystem, name, parent):
        FilesystemObject.__init__(self, filesystem, name, parent)
        self.contents = []

    def __repr__(self):
        return self.name

    @property
    def size(self):
        result = 0

        for child in self.contents:
            result += child.size

        return result

    def add_directory(self, name):
        self.contents.append(Directory(self.filesystem, name, self))

    def add_file(self, name, size):
        self.contents.append(File(self.filesystem, name, size, self))

    def child_directory(self, name):
        if name == "..":
            return self.parent

        for child in self.contents:
            if child.name == name and isinstance(child, Directory):
                return child

        raise ValueError("Unknown child directory", name)

    def walk_print(self, indent):
        result = "%s- %s" % (" " * indent, self.name)

        print("%s (dir, total_size=%d)" % (result, self.size))
        for content in self.contents:
            content.walk(indent + 1)

    def directories_smaller_than(self, limit):
        if self.size < limit:
            yield self

        for content in self.contents:
            if isinstance(content, Directory):
                for directory in content.directories_smaller_than(limit):
                    yield directory

    def directories_bigger_than(self, limit):
        if self.size > limit:
            yield self

        for content in self.contents:
            if isinstance(content, Directory):
                for directory in content.directories_bigger_than(limit):
                    yield directory


class File(FilesystemObject):
    def __init__(self, filesystem, name, size, parent):
        FilesystemObject.__init__(self, filesystem, name, parent)
        self.size = size

    def __repr__(self):
        return "%s (%d)" % (self.name, self.size)

    def walk_print(self, indent):
        result = "%s- %s" % (" " * indent, self.name)

        print("%s (file, size=%d)" % (result, self.size))


class Filesystem(object):
    def __init__(self):
        self.root = Directory(self, "/", None)
        self.current_directory = self.root

    def chdir(self, target):
        if target == "/":
            self.current_directory = self.root
        else:
            self.current_directory = self.current_directory.child_directory(target)

    def execute(self, command):
        if command.startswith("cd"):
            chdir, target = command.split(" ")
            self.chdir(target)
        elif command == "ls":
            # nothing to be done here, really
            pass
        else:
            raise ValueError("Unknown command %s" % (command,))

    def walk_print(self):
        self.root.walk_print(indent=0)

    def directories_smaller_than(self, limit):
        for big_directory in self.root.directories_smaller_than(limit):
            yield big_directory

    def directories_bigger_than(self, limit):
        for big_directory in self.root.directories_bigger_than(limit):
            yield big_directory


class Tree(object):
    def __init__(self, trees, column, row, height, visible=False):
        self.column = column
        self.row = row
        self.trees = trees
        self.height = height
        self.visible = visible
        self.scenic_score = None

    def __repr__(self):
        if self.visible:
            return "%d" % (self.height,)

        return "#"

    def __check_left_visibility(self):
        for x in range(self.column - 1, -1, -1):
            if self.trees[self.row][x].height >= self.height:
                # print("\tNot visible because", x, self.row, "is taller or equal")
                return False

        # print("\tVisible from the left")
        return True

    def __check_right_visibility(self):
        for x in range(self.column + 1, len(self.trees[self.row])):
            if self.trees[self.row][x].height >= self.height:
                # print("\tNot visible because", x, self.row, "is taller or equal")
                return False

        # print("\tVisible from the right")
        return True

    def __check_top_visibility(self):
        for y in range(self.row - 1, -1, -1):
            if self.trees[y][self.column].height >= self.height:
                # print("\tNot visible because", self.column, y, "is taller or equal")
                return False

        # print("\tVisible from the top")
        return True

    def __check_bottom_visibility(self):
        for y in range(self.row + 1, len(self.trees)):
            if self.trees[y][self.column].height >= self.height:
                # print("\tNot visible because", self.column, y, "is taller or equal")
                return False

        # print("\tVisible from the bottom")
        return True

    def __check_edge_visibility(self):
        if self.column == 0 or self.row == 0:
            # print("\tThis is an edge tree")
            return True

        if self.column == len(self.trees[0]) - 1 or self.row == len(self.trees) - 1:
            # print("\tThis is an edge tree")
            return True

        return False

    def check_visibility(self):
        # print("checking", self.column, self.row, "with height", self.height)
        self.visible = self.__check_edge_visibility() or self.__check_top_visibility() \
                       or self.__check_bottom_visibility() or self.__check_left_visibility() \
                       or self.__check_right_visibility()

    def __check_left_score(self):
        score = 0

        for x in range(self.column - 1, -1, -1):
            tree = self.trees[self.row][x]
            if tree.height >= self.height:
                # print("\t", self.column, self.row, "can finally left see", x, self.row, "with height", tree.height)
                return score + 1

            # print("\t", self.column, self.row, "can left see", x, self.row, "with height", tree.height)
            score += 1

        # print("\t", self.column, self.row, "reached the edge visibility with", score)
        return score

    def __check_right_score(self):
        score = 0

        for x in range(self.column + 1, len(self.trees[self.row])):
            tree = self.trees[self.row][x]
            if tree.height >= self.height:
                # print("\t", self.column, self.row, "can finally right see", x, self.row, "with height", tree.height)
                return score + 1

            # print("\t", self.column, self.row, "can right see", x, self.row, "with height", tree.height)
            score += 1

        # print("\t", self.column, self.row, "reached the edge visibility with", score)
        return score

    def __check_top_score(self):
        score = 0

        for y in range(self.row - 1, -1, -1):
            tree = self.trees[y][self.column]
            if tree.height >= self.height:
                # print("\t", self.column, self.row, "can finally top see", self.column, y, "with height", tree.height)
                return score + 1

            # print("\t", self.column, self.row, "can top see", self.column, y, "with height", tree.height)
            score += 1

        # print("\t", self.column, self.row, "reached the edge visibility with", score)
        return score

    def __check_bottom_score(self):
        score = 0

        for y in range(self.row + 1, len(self.trees)):
            tree = self.trees[y][self.column]
            if tree.height >= self.height:
                # print("\t", self.column, self.row, "can finally bottom see", self.column, y, "with height",
                # tree.height)
                return score + 1

            # print("\t", self.column, self.row, "can bottom see", self.column, y, "with height", tree.height)
            score += 1

        # print("\t", self.column, self.row, "reached the edge visibility with", score)
        return score

    def check_scenic_score(self):
        # print("checking", self.column, self.row, "with height", self.height)

        top = self.__check_top_score()
        bottom = self.__check_bottom_score()
        left = self.__check_left_score()
        right = self.__check_right_score()

        self.scenic_score = top * bottom * left * right
        # print("\tscenic score is (top=%d * left=%d * right=%d * bottom=%d) = %d" % (
        #     top, left, right, bottom, self.scenic_score))


class Rope(object):
    def __init__(self, knots=1):
        self.head_position = (0, 0)
        self.pivot = self.head_position
        self.knots = []
        self.tail_positions = set()

        for knot in range(knots):
            self.knots.append((0, 0))
        self.tail_positions.add((0, 0))

    def print_status(self, separator="=" * 50):
        head_x, head_y = self.head_position

        max_x = max(head_x, max(k[0] for k in self.knots))
        max_y = max(head_y, max(k[1] for k in self.knots))

        print(separator)
        lines = []
        for y in range(max_y + 1):
            line = ""

            for x in range(max_x + 1):
                if (x, y) == (head_x, head_y):
                    line += "H"
                elif (x, y) in self.knots:
                    position = self.knots.index((x, y))
                    line += str(position)
                else:
                    line += "."

            lines.append(line)

        for line in lines[::-1]:
            print(line)
        print(separator)
        print("")

    def distance_to_pivot(self, index):
        head_x, head_y = self.pivot
        x, y = self.knots[index]

        return max(abs(x - head_x), abs(y - head_y))

    def move_towards_pivot(self, index):
        pivot_x, pivot_y = self.pivot
        knot_x, knot_y = self.knots[index]

        if pivot_x > knot_x:
            knot_x += 1
        elif pivot_x < knot_x:
            knot_x -= 1
        if pivot_y > knot_y:
            knot_y += 1
        elif pivot_y < knot_y:
            knot_y -= 1

        self.knots[index] = (knot_x, knot_y)

    def move(self, direction):
        if direction == "R":
            self.head_position = (self.head_position[0] + 1, self.head_position[1])
        elif direction == "L":
            self.head_position = (self.head_position[0] - 1, self.head_position[1])
        elif direction == "U":
            self.head_position = (self.head_position[0], self.head_position[1] + 1)
        elif direction == "D":
            self.head_position = (self.head_position[0], self.head_position[1] - 1)
        else:
            raise ValueError("Unknown direction to move rope: %s" % (direction,))

        for index in range(len(self.knots)):
            if index > 0:
                self.pivot = self.knots[index - 1]
            else:
                self.pivot = self.head_position

            if self.distance_to_pivot(index) > 1:
                self.move_towards_pivot(index)

        tail_x, tail_y = self.knots[len(self.knots) - 1]
        self.tail_positions.add((tail_x, tail_y))


class VideoCPU(object):
    INSTRUCTION_CYCLES = {
        "noop": 1,
        "add": {
            "x": 2
        }
    }
    RELEVANT_CYCLES = [
        20, 60, 100, 140, 180, 220
    ]
    DRAWING_CYCLES = [
        40, 80, 120, 160, 200, 240
    ]

    def __init__(self):
        self.cycle = 0
        self.registers = {}
        self.relevant_strenghts = {}
        self.screen = []

    def __draw(self):
        position = self.registers.get("x", 1)
        if len(self.screen) == 0:
            current_screen = ""
            self.screen.append("")
        else:
            current_screen = self.screen[-1]

        current_draw_index = len(current_screen)
        if current_draw_index in [position - 1, position, position + 1]:
            new_pixel = "#"
        else:
            new_pixel = "."

        current_screen += new_pixel
        self.screen[-1] = current_screen

        if self.cycle in VideoCPU.DRAWING_CYCLES:
            self.screen.append("")

    def __increase_cycle(self, amount):
        for _ in range(amount):
            self.cycle += 1

            if self.cycle in VideoCPU.RELEVANT_CYCLES:
                self.relevant_strenghts[self.cycle] = {}
                for register in self.registers:
                    self.relevant_strenghts[self.cycle][register] = self.registers[register] * self.cycle

            self.__draw()

    def no_op(self):
        self.__increase_cycle(VideoCPU.INSTRUCTION_CYCLES["noop"])

    def add(self, register, amount):
        self.__increase_cycle(VideoCPU.INSTRUCTION_CYCLES["add"].get(register, 2))
        self.registers[register] = self.registers.get(register, 1) + amount


class MonkeyTest(object):
    def __init__(self, predicate, true_case, false_case):
        self.predicate = predicate
        self.true_case = true_case
        self.false_case = false_case

        self.divisor = int(self.predicate[len("divisible by"):].strip())

    def __repr__(self):
        return "MonkeyTest{Predicate=%s; True=%d; False=%d}" % (self.predicate, self.true_case, self.false_case)

    def perform(self, item):
        if self.predicate.startswith("divisible by"):
            return item.value % self.divisor == 0
        else:
            raise ValueError("Unknown test predicate %s" % (self.predicate,))


class MonkeyItem(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "MonkeyItem{Value=%d}" % (self.value,)

    def boredom(self):
        self.value = int(self.value / 3)

    def mega_boredom(self, divisor):
        self.value = self.value % divisor


class Monkey(object):
    def __init__(self, tag, items, operation, test):
        self.tag = tag
        self.items = items
        self.operation = operation
        self.test = test
        self.inspection_count = 0
        self.divisor = self.test.divisor

    def __repr__(self):
        return "Monkey{Tag=%d; Items=%s; Operation=%s; Test=%s}" % (
            self.tag, self.items, self.operation, self.test)

    def do_operation(self, item):
        right_hand = self.operation.split("=")[1].strip()
        left, operator, right = right_hand.split(" ")

        if left == "old":
            left_value = item.value
        else:
            left_value = int(left)

        if right == "old":
            right_value = item.value
        else:
            right_value = int(right)

        if operator == "*":
            new_value = left_value * right_value
        elif operator == "+":
            new_value = left_value + right_value
        else:
            raise ValueError("Unknown operator %s" % (operator,))

        item.value = new_value


class IntoTheAbyss(Exception): pass


class NowhereToDrop(Exception): pass


class Cave(object):
    def __init__(self):
        self.contents = {}
        self.bounds = None

        self.__sand_generator = None

    def __update_bounds(self, x, y):
        if self.bounds is None:
            self.bounds = (x, y, x, y)
        else:
            self.bounds = (
                min(x, self.bounds[0]),
                min(y, self.bounds[1]),
                max(x, self.bounds[2]),
                max(y, self.bounds[3])
            )

    @property
    def sand_generator(self):
        if self.__sand_generator is not None:
            return self.__sand_generator

        for x in self.contents:
            for y in self.contents[x]:
                if isinstance(self.contents[x][y], CaveSandGenerator):
                    self.__sand_generator = self.contents[x][y]
                    return self.__sand_generator

        return None

    def add(self, x, y, object_class):
        if x not in self.contents:
            self.contents[x] = {}

        instance = object_class(self, x, y)
        self.contents[x][y] = instance
        self.__update_bounds(x, y)

        return instance

    def set(self, x, y, instance):
        self.contents[x][y] = instance

        return instance

    def object_at(self, x, y):
        if x not in self.contents:
            return None
        if y not in self.contents[x]:
            return None

        return self.contents[x][y]

    def out_of_bounds(self, x, y):
        x0, y0, x1, y1 = self.bounds
        return x < x0 or x > x1 or y < y0 or y > y1

    def __repr__(self):
        result = ""

        for y in range(self.bounds[1], self.bounds[3] + 1):
            line = ""
            for x in range(self.bounds[0], self.bounds[2] + 1):
                line = "%s%s" % (line, self.contents[x][y])
            result = "%s%s\n" % (result, line)

        return result


class CaveObject(object):
    def __init__(self, cave, x, y):
        self.cave = cave
        self.x = x
        self.y = y

    def drop_coordinates(self):
        possibilities = [
            (self.x, self.y + 1),
            (self.x - 1, self.y + 1),
            (self.x + 1, self.y + 1)
        ]

        for possibility in possibilities:
            x, y = possibility
            if isinstance(self.cave.object_at(x, y), CaveAir):
                return x, y
            if self.cave.out_of_bounds(x, y):
                raise IntoTheAbyss()

        return None


class CaveSandGenerator(CaveObject):
    def __init__(self, cave, x, y):
        CaveObject.__init__(self, cave, x, y)

    def __repr__(self):
        return "+"

    def generate(self):
        result = self.drop_coordinates()
        if result is None:
            raise NowhereToDrop()

        x, y = result
        sand = self.cave.add(x, y, CaveSand)
        sand.drop()


class CaveAir(CaveObject):
    def __init__(self, cave, x, y):
        CaveObject.__init__(self, cave, x, y)

    def __repr__(self):
        return "."


class CaveRock(CaveObject):
    def __init__(self, cave, x, y):
        CaveObject.__init__(self, cave, x, y)

    def __repr__(self):
        return "#"


class CaveSand(CaveObject):
    def __init__(self, cave, x, y):
        CaveObject.__init__(self, cave, x, y)

    def __repr__(self):
        return "o"

    def drop(self):
        coordinates = self.drop_coordinates()
        while coordinates is not None:
            x, y = coordinates

            self.cave.add(self.x, self.y, CaveAir)

            self.x, self.y = x, y
            self.cave.set(x, y, self)

            coordinates = self.drop_coordinates()
