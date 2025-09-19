package pt.dmb.adventofcode.y2016.p02

import pt.dmb.adventofcode.common.Utilities

class PartOne {
}

fun main() {
    Utilities.readInputFile(2016, 2, scope = "main").forEach { line ->
        val solver = PartOne()
        TODO()
    }
}

/*
import common

if __name__ == "__main__":
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for input_file in common.inputs:
        row_index = 1
        column_index = 1
        code = ""

        for line in common.read_file(input_file):
            for instruction in line:
                if instruction == "U":
                    row_index = max(0, row_index - 1)
                elif instruction == "D":
                    row_index = min(2, row_index + 1)
                elif instruction == "L":
                    column_index = max(0, column_index - 1)
                elif instruction == "R":
                    column_index = min(2, column_index + 1)

            code += str(keypad[row_index][column_index])

        print(code)

84452
 */