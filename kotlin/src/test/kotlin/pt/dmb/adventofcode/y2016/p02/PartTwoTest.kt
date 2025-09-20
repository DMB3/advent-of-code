package pt.dmb.adventofcode.y2016.p02

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartTwoTest {
    @Test
    fun `Should return correct solution`() {
        val partTwo = PartTwo()

        Utilities.readInputFile(2016, 2).forEach { line ->
            line.forEach { instruction ->
                partTwo.readInstruction(instruction)
            }

            partTwo.updateCode()
        }

        assertEquals("5DB3", partTwo.code())
    }
}
