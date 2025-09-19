package pt.dmb.adventofcode.y2015.p03

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartOneTest {
    @Test
    fun `Should return correct solution`() {
        val allResults = mutableListOf<Int>()

        Utilities.readInputFile(2015, 3).forEach { line ->
            val solver = PartOne()

            line.toCharArray().forEach { char ->
                solver.parseInstruction(char)
            }

            allResults.add(solver.seenLength())
        }

        assertEquals(
            allResults, listOf(
                2,
                4,
                2,
                2,
            )
        )
    }
}