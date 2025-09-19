package pt.dmb.adventofcode.y2015.p05

import pt.dmb.adventofcode.common.Utilities

class PartTwo {
    private var nices = 0

    fun isNice(test: String): Boolean {
        var foundDuplicatePair = false
        for (a in 0 until test.length - 1) {
            val oneTwo = test[a].toString() + test[a + 1].toString()
            if (oneTwo in test.substring(a + 2)) {
                foundDuplicatePair = true
                break
            }
        }

        if (!foundDuplicatePair) return false

        var index = 0
        while (index < test.length - 2) {
            if (test[index] == test[index + 2]) {
                return true
            }
            index++
        }

        return false
    }

    fun increaseNices() {
        nices++
    }

    fun countNices() = nices
}

fun main() {
    val solver = PartTwo()
    Utilities.readInputFile(2015, 5, scope = "main").forEach { line ->
        if (solver.isNice(line)) {
            solver.increaseNices()
        }
    }
    println(solver.countNices())
}