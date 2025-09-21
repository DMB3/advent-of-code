package pt.dmb.adventofcode.y2016.p03

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartOneTest {
    @Test
    fun `Should return correct solution`() {
        val partOne = PartOne()

        Utilities.readInputFile(2016, 3).forEach { line ->
            val splitLine = line.trim().split("\\s+".toRegex())

            val one = splitLine[0].toInt()
            val two = splitLine[1].toInt()
            val three = splitLine[2].toInt()

            partOne.increaseIfNeeded(one, two, three)
        }

        assertEquals(3, partOne.possibles())
    }
}
