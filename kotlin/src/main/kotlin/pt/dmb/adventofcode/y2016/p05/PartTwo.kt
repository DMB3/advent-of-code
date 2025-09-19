package pt.dmb.adventofcode.y2016.p05

import pt.dmb.adventofcode.common.Utilities

class PartTwo

fun main() {
    Utilities.readInputFile(2016, 5, scope = "main").forEach { line ->
        val solver = PartTwo()
        TODO()
    }
}

/*
from hashlib import md5

import common

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)

        for line in common.read_file(input_file):
            test_value = 1
            character_positions = {}

            while True:
                test = line + str(test_value)
                test_md5 = md5(test.encode("utf-8")).hexdigest()
                test_value += 1

                if test_md5.startswith("00000"):
                    try:
                        position = int(test_md5[5])
                    except ValueError:
                        continue
                    if position >= 8:
                        continue
                    if position in character_positions:
                        continue

                    character = test_md5[6]
                    print("character", character, "at position", position)
                    character_positions[position] = character

                    if len(character_positions) == 8:
                        sorted_positions = sorted(character_positions.keys())
                        password = ""
                        for position in sorted_positions:
                            password += character_positions[position]
                        print(password)
                        break

character a at position 6
character b at position 7
character 1 at position 5
character 8 at position 0
character 5 at position 3
character c at position 1
character d at position 4
character 3 at position 2
8c35d1ab

 */
