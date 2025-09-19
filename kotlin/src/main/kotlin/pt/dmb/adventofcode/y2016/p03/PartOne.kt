package pt.dmb.adventofcode.y2016.p03

import pt.dmb.adventofcode.common.Utilities

class PartOne {
}

fun main() {
    Utilities.readInputFile(2016, 3, scope = "main").forEach { line ->
        val solver = PartOne()
        TODO()
    }
}

/*
import common

if __name__ == "__main__":
    for input_file in common.inputs:
        possibles = 0

        for line in common.read_file(input_file):
            one, two, three = line.split()
            if int(one) < int(two) + int(three) and \
                    int(two) < int(one) + int(three) and \
                    int(three) < int(one) + int(two):
                possibles += 1

        print(possibles)

1032
 */