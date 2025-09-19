package pt.dmb.adventofcode.y2015.p01

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartOneTest {
    @Test
    fun `Should return correct solution`() {
        val allResults = mutableListOf<Int>()

        Utilities.readInputFile(2015, 1).forEach { line ->
            val partOne = PartOne()
            line.toCharArray().forEach { char ->
                partOne.parseInstruction(char)
            }
            allResults.add(partOne.floor())
        }

        assertEquals(
            allResults, listOf(
                0,
                0,
                3,
                3,
                3,
                -1,
                -1,
                -3,
                -3,
                -1,
                -1,
            )
        )
    }
}
