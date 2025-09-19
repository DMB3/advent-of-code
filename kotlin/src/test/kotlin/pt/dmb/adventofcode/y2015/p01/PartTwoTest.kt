package pt.dmb.adventofcode.y2015.p01

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartTwoTest {
    @Test
    fun `Should return correct solution`() {
        val allResults = mutableListOf<Int>()

        Utilities.readInputFile(2015, 1).forEach { line ->
            val partTwo = PartTwo()
            line.toCharArray().forEach { char ->
                if (partTwo.parseInstruction(char)) {
                    allResults.add(partTwo.position())
                    return
                }
            }
        }

        assertEquals(
            allResults,
            listOf(
                1,
                3,
                1,
                1,
                1,
                1,
                5,
            ),
        )
    }
}
