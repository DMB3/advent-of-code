package pt.dmb.adventofcode.y2015.p02

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartOneTest {
    @Test
    fun `Should return correct solution`() {
        var result = 0

        Utilities.readInputFile(2015, 2).forEach { line ->
            val splits = line.split("x")

            val length = splits[0].toInt()
            val width = splits[1].toInt()
            val height = splits[2].toInt()

            val solver = PartOne(length, width, height)

            result += solver.area() + solver.minSide()
        }

        assertEquals(101, result)
    }
}