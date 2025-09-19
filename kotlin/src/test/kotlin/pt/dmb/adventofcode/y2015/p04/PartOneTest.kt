package pt.dmb.adventofcode.y2015.p04

import org.junit.jupiter.api.Test
import pt.dmb.adventofcode.common.Utilities
import kotlin.test.assertEquals

class PartOneTest {
    @Test
    fun `Should return correct solution`() {
        val allResults = mutableListOf<String>()

        Utilities.readInputFile(2015, 4).forEach { line ->
            val solver = PartOne()

            while (true) {
                if (solver.process(line)) {
                    break
                }
            }

            allResults.add(solver.getSolution())
        }

        assertEquals(
            allResults, listOf(
                "abcdef 609043 000001dbbfa3a5c83a2d506429c7b00e",
                "pqrstuv 1048970 000006136ef2ff3b291c85725f17325c",
            )
        )
    }
}