package pt.dmb.adventofcode.y2016.p01

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartOneTest {
    @Test
    fun `Should return correct solution`() {
        val allResults = mutableListOf<Pair<Pair<Int, Int>, Int>>()

        Utilities.readInputFile(2016, 1).forEach { line ->
            val partOne = PartOne()

            line.split(",").forEach { instruction ->
                val direction = instruction.trim()[0]
                val amount = instruction.trim().substring(1).toInt()

                partOne.sleigh.turn(direction)
                partOne.sleigh.walk(amount)
            }

            allResults.add(Pair(partOne.sleigh.location(), partOne.distance()))
        }

        assertEquals(
            allResults,
            listOf(
                Pair(Pair(2, -3), 5),
                Pair(Pair(0, 2), 2),
                Pair(Pair(10, -2), 12),
                Pair(Pair(4, -4), 8),
            ),
        )
    }
}
