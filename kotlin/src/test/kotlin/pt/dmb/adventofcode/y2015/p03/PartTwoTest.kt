package pt.dmb.adventofcode.y2015.p03

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartTwoTest {
    @Test
    fun `Should return correct solution`() {
        val allResults = mutableListOf<Int>()

        Utilities.readInputFile(2015, 3).forEach { line ->
            val solver = PartTwo()

            line.toCharArray().forEach { char ->
                solver.parseInstruction(char)
            }

            allResults.add(solver.seenLength())
        }

        assertEquals(
            allResults,
            listOf(
                2,
                3,
                11,
                3,
            ),
        )
    }
}
