package pt.dmb.adventofcode.y2016.p05

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities

class PartTwoTest {
    @Test
    fun `Should return correct solution`() {
        val allResults = mutableListOf<Int>()

        Utilities.readInputFile(2016, 5).forEach { line ->
            val partOne = PartOne()
            line.toCharArray().forEach { char ->
                // TODO
            }

            TODO()
        }
    }
}

/*
character 5 at position 1
character e at position 4
character 3 at position 7
character c at position 3
character 0 at position 0
character e at position 6
character 8 at position 5
character a at position 2
05ace8e3
 */