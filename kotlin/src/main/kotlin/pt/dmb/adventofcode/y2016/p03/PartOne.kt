package pt.dmb.adventofcode.y2016.p03

import pt.dmb.adventofcode.common.Utilities

class PartOne {
    private var possibles = 0

    fun increaseIfNeeded(one: Int, two: Int, three: Int) {
        if ((one < two + three) && (two < one + three) && (three < one + two)) {
            possibles++
        }
    }

    fun possibles() = possibles
}

fun main() {
    val solver = PartOne()

    Utilities.readInputFile(2016, 3, scope = "main").forEach { line ->
        val splitLine = line.trim().split("\\s+".toRegex())

        val one = splitLine[0].toInt()
        val two = splitLine[1].toInt()
        val three = splitLine[2].toInt()

        solver.increaseIfNeeded(one, two, three)
    }

    println(solver.possibles())
}