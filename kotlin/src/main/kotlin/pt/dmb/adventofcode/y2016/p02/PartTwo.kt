package pt.dmb.adventofcode.y2016.p02

import pt.dmb.adventofcode.common.Utilities

class PartTwo

fun main() {
    Utilities.readInputFile(2016, 2, scope = "main").forEach { line ->
        val solver = PartTwo()
        TODO()
    }
}

/*
import common

if __name__ == "__main__":
    keypad = {
        "1": {
            "D": "3"
        },
        "2": {
            "D": "6",
            "R": "3"
        },
        "3": {
            "U": "1",
            "D": "7",
            "L": "2",
            "R": "4"
        },
        "4": {
            "D": "8",
            "L": "3"
        },
        "5": {
            "R": "6"
        },
        "6": {
            "U": "2",
            "D": "A",
            "L": "5",
            "R": "7"
        },
        "7": {
            "U": "3",
            "D": "B",
            "L": "6",
            "R": "8"
        },
        "8": {
            "U": "4",
            "D": "C",
            "L": "7",
            "R": "9"
        },
        "9": {
            "L": "8"
        },
        "A": {
            "U": "6",
            "R": "B"
        },
        "B": {
            "U": "7",
            "D": "D",
            "L": "A",
            "R":"C"
        },
        "C": {
            "U": "8",
            "L": "B",
        },
        "D": {
            "U": "B"
        }
    }

    for input_file in common.inputs:
        current_key = "5"
        code = ""

        for line in common.read_file(input_file):
            for instruction in line:
                current_key = keypad.get(current_key).get(instruction, current_key)

            code += current_key

        print(code)

D65C3
 */
