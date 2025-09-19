package pt.dmb.adventofcode.y2016.p01

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities

class PartOneTest {
    @Test
    fun `Should return correct solution`() {
        val allResults = mutableListOf<Int>()

        Utilities.readInputFile(2016, 1).forEach { line ->
            val partOne = PartOne()
            line.toCharArray().forEach { char ->
                // TODO
            }

            TODO()
        }
    }
}

/*
Ended at (2, -3) which is 5 away
Ended at (0, 2) which is 2 away
Ended at (10, -2) which is 12 away
Ended at (4, -4) which is 8 away
 */