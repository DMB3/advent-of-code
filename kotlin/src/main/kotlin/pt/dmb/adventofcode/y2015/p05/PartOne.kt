package pt.dmb.adventofcode.y2015.p05

import pt.dmb.adventofcode.common.Utilities

class PartOne {
    private var nices = 0

    fun isNice(test: String): Boolean {
        val forbidden = listOf("ab", "cd", "pq", "xy")
        forbidden.forEach { nope ->
            if (test.contains(nope)) return false
        }

        val vowels = test.filter { it in "aeiouAEIOU" }
        if (vowels.length < 3) return false

        var hasDupe = false
        for (a in 0 until test.length - 1) {
            if (test[a] == test[a + 1]) {
                hasDupe = true
                break
            }
        }
        if (!hasDupe) return false

        return true
    }

    fun increaseNices() {
        nices++
    }

    fun countNices() = nices
}

fun main() {
    val solver = PartOne()
    Utilities.readInputFile(2015, 5, scope = "main").forEach { line ->
        if (solver.isNice(line)) {
            solver.increaseNices()
        }
    }
    println(solver.countNices())
}