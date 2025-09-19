package pt.dmb.adventofcode.y2016.p04

import pt.dmb.adventofcode.common.Utilities

class PartOne

fun main() {
    Utilities.readInputFile(2016, 4, scope = "main").forEach { line ->
        val solver = PartOne()
        TODO()
    }
}

/*
import common

if __name__ == "__main__":
    for input_file in common.inputs:
        real_count = 0
        sector_total = 0

        for line in common.read_file(input_file):
            parts = line.split("-")

            sector_and_checksum = parts.pop()
            sector = int(sector_and_checksum[:sector_and_checksum.find("[")])
            checksum = sector_and_checksum[(sector_and_checksum.find("[") + 1):][:-1]

            letters_and_counts = {}
            for part in parts:
                no_dupes = "".join(set(part))
                for character in no_dupes:
                    if character not in letters_and_counts:
                        letters_and_counts[character] = 0
                    letters_and_counts[character] += part.count(character)

            counts_and_letters = {}
            sorted_counts = set()
            for letter in letters_and_counts:
                count = letters_and_counts[letter]
                sorted_counts.add(count)

                if count not in counts_and_letters:
                    counts_and_letters[count] = []
                counts_and_letters[count].append(letter)
                counts_and_letters[count] = sorted(counts_and_letters[count])
            sorted_counts = sorted(sorted_counts)[::-1]

            expected_checksum = ""
            for count in sorted_counts:
                expected_checksum += "".join(counts_and_letters[count])
            expected_checksum = expected_checksum[:5]

            if expected_checksum == checksum:
                real_count += 1
                sector_total += sector

        print(real_count, "real checksums for a total sector sum of", sector_total)

301 real checksums for a total sector sum of 173787
 */
