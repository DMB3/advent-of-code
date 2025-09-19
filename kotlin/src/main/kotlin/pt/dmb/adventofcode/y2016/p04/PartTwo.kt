package pt.dmb.adventofcode.y2016.p04

import pt.dmb.adventofcode.common.Utilities

class PartTwo

fun main() {
    Utilities.readInputFile(2016, 4, scope = "main").forEach { line ->
        val solver = PartTwo()
        TODO()
    }
}

/*
import common


def rotate_letter(letter, times):
    root_ord = ord("a")
    top_ord = ord("z")

    current_ord = ord(letter)
    for time in range(times):
        current_ord += 1
        if current_ord > top_ord:
            current_ord = root_ord

    return chr(current_ord)


if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        for line in common.read_file(input_file):
            parts = line.split("-")

            sector_and_checksum = parts.pop()
            sector = int(sector_and_checksum[:sector_and_checksum.find("[")])
            checksum = sector_and_checksum[(sector_and_checksum.find("[") + 1):][:-1]

            result = ""
            for part in parts:
                for letter in part:
                    result += rotate_letter(letter, sector)

            if result.find("northpole") > -1:
                print("\t", result, sector)

northpoleobjectstorage 548
 */
