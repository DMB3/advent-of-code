package pt.dmb.adventofcode.y2015.p05

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartOneTest {
    @Test
    fun `Should return correct solution`() {
        val solver = PartOne()

        Utilities.readInputFile(2015, 5).forEach { line ->
            if (solver.isNice(line)) {
                solver.increaseNices()
            }
        }

        assertEquals(0, solver.countNices())
    }
}