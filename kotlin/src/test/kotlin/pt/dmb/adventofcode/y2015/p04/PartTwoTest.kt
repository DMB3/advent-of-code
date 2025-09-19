package pt.dmb.adventofcode.y2015.p04

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartTwoTest {
    @Test
    fun `Should return correct solution`() {
        val allResults = mutableListOf<String>()

        Utilities.readInputFile(2015, 4).forEach { line ->
            val solver = PartTwo()

            while (true) {
                if (solver.process(line)) {
                    break
                }
            }

            allResults.add(solver.getSolution())
        }

        assertEquals(
            allResults,
            listOf(
                "abcdef 6742839 000000072a1e4320d13deee9d934ae29",
                "pqrstuv 5714438 000000c76bdbbb114044ada5ad14523b",
            ),
        )
    }
}
