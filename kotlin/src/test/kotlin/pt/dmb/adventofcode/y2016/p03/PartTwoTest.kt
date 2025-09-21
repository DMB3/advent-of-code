package pt.dmb.adventofcode.y2016.p03

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartTwoTest {
    @Test
    fun `Should return correct solution`() {
        val partTwo = PartTwo()

        Utilities.readInputFile(2016, 3).forEach { line ->
            val splitLine = line.trim().split("\\s+".toRegex())

            val one = splitLine[0].toInt()
            val two = splitLine[1].toInt()
            val three = splitLine[2].toInt()

            partTwo.addLine(one, two, three)
        }

        partTwo.lines().forEach { it ->
            for (index in 0..2) {
                val one = it[0][index]
                val two = it[1][index]
                val three = it[2][index]

                partTwo.increaseIfNeeded(one, two, three)
            }
        }

        assertEquals(6, partTwo.possibles())
    }
}
