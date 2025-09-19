package pt.dmb.adventofcode.y2016.p01

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities

class PartTwoTest {
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
R2, L3
R2, R2, R2
R5, L5, R5, R3
R8, R4, R4, R8
Repeated at (4, 0) which is 4 steps away
 */