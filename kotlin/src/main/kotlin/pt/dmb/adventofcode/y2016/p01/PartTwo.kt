package pt.dmb.adventofcode.y2016.p01

import pt.dmb.adventofcode.common.Utilities

class PartTwo

fun main() {
    Utilities.readInputFile(2016, 1, scope = "main").forEach { line ->
        val solver = PartTwo()
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


def walk(location, direction, steps, seen):
    if direction == NORTH:
        for i in range(steps, 0, -1):
            new_location = (location[0], location[1] - i)
            if new_location in seen:
                return new_location, True
            seen.add(new_location)

        return (location[0], location[1] - steps), False
    elif direction == SOUTH:
        for i in range(1, steps):
            new_location = (location[0], location[1] + i)
            if new_location in seen:
                return new_location, True
            seen.add(new_location)

        return (location[0], location[1] + steps), False
    elif direction == EAST:
        for i in range(1, steps):
            new_location = (location[0] + i, location[1])
            if new_location in seen:
                return new_location, True
            seen.add(new_location)

        return (location[0] + steps, location[1]), False
    elif direction == WEST:
        for i in range(steps, 0, -1):
            new_location = (location[0] - i, location[1])
            if new_location in seen:
                return new_location, True
            seen.add(new_location)

        return (location[0] - steps, location[1]), False

    raise ValueError("Unknown direction facing %s to walk %s at %s" % (direction, steps, location))


if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)

        for line in common.read_file(input_file):
            print(line)
            facing = NORTH
            location = (0, 0)
            seen = set()
            seen.add(location)

            for instruction in line.split(","):
                direction, amount = instruction.strip()[0], int(instruction.strip()[1:])
                facing = turn(direction, facing)
                location, stop = walk(location, facing, amount, seen)
                if stop:
                    distance = abs(location[0]) + abs(location[1])
                    print("Repeated at", location, "which is", distance, "steps away")
                    break

                seen.add(location)

R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4, L1, R4, R5, L3, R5, L1, R3, L5, R1, L2, R1, L5, L1, R1, R4, R1, L1, L3, R3, R5, L3, R4, L4, R5, L5, L1, L2, R4, R3, R3, L185, R3, R4, L5, L4, R48, R1, R2, L1, R1, L4, L4, R77, R5, L2, R192, R2, R5, L4, L5, L3, R2, L4, R1, L5, R5, R4, R1, R2, L3, R4, R4, L2, L4, L3, R5, R4, L2, L1, L3, R1, R5, R5, R2, L5, L2, L3, L4, R2, R1, L4, L1, R1, R5, R3, R3, R4, L1, L4, R1, L2, R3, L3, L2, L1, L2, L2, L1, L2, R3, R1, L4, R1, L1, L4, R1, L2, L5, R3, L5, L2, L2, L3, R1, L4, R1, R1, R2, L1, L4, L4, R2, R2, R2, R2, R5, R1, L1, L4, L5, R2, R4, L3, L5, R2, R3, L4, L1, R2, R3, R5, L2, L3, R3, R1, R3
Repeated at (-22, -136) which is 158 steps away

 */
