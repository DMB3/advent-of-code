package pt.dmb.adventofcode.y2016.p01

import pt.dmb.adventofcode.common.Utilities

class PartOne {
}

fun main() {
    Utilities.readInputFile(2016, 1, scope = "main").forEach { line ->
        val solver = PartOne()
        TODO()
    }
}

/*
import common

NORTH, SOUTH, EAST, WEST = 0, 1, 2, 3
LEFT, RIGHT = "L", "R"


def turn(direction, facing):
    if facing == NORTH:
        return EAST if direction == RIGHT else WEST
    elif facing == SOUTH:
        return WEST if direction == RIGHT else EAST
    elif facing == EAST:
        return SOUTH if direction == RIGHT else NORTH
    elif facing == WEST:
        return NORTH if direction == RIGHT else SOUTH

    raise ValueError("Unknown direction facing %s to turn %s" % (facing, direction))


def walk(location, direction, steps):
    if direction == NORTH:
        return location[0], location[1] - steps
    elif direction == SOUTH:
        return location[0], location[1] + steps
    elif direction == EAST:
        return location[0] + steps, location[1]
    elif direction == WEST:
        return location[0] - steps, location[1]

    raise ValueError("Unknown direction facing %s to walk %s at %s" % (direction, steps, location))


if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)

        for line in common.read_file(input_file):
            facing = NORTH
            location = (0, 0)

            for instruction in line.split(","):
                direction, amount = instruction.strip()[0], int(instruction.strip()[1:])
                facing = turn(direction, facing)
                location = walk(location, facing, amount)

            distance = abs(location[0]) + abs(location[1])
            print("Ended at", location, "which is", distance, "away")

Ended at (-151, -147) which is 298 away
 */