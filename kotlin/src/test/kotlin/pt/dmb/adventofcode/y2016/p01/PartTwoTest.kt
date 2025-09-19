package pt.dmb.adventofcode.y2016.p01

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartTwoTest {
    @Test
    fun `Should return correct solution`() {
        Utilities.readInputFile(2016, 1).forEach { line ->
            val partTwo = PartTwo()

            line.split(",").forEach { instruction ->
                val direction = instruction.trim()[0]
                val amount = instruction.trim().substring(1).toInt()

                partTwo.sleigh.turn(direction)
                partTwo.sleigh.walk(amount)
                if (partTwo.sleigh.shouldStop()) {
                    assertEquals(Pair(4, 0), partTwo.sleigh.location())
                    assertEquals(4, partTwo.distance())
                    return
                }

                partTwo.sleigh.addSeenLocation(partTwo.sleigh.location())
            }
        }
    }
}
