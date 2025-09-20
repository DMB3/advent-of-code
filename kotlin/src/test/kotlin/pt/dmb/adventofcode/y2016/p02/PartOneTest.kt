package pt.dmb.adventofcode.y2016.p02

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartOneTest {
    @Test
    fun `Should return correct solution`() {
        val partOne = PartOne()

        Utilities.readInputFile(2016, 2).forEach { line ->
            line.forEach { instruction ->
                partOne.readInstruction(instruction)
            }

            partOne.updateCode()
        }

        assertEquals("1985", partOne.code())
    }
}
