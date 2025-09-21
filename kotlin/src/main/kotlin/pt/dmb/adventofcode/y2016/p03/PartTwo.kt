package pt.dmb.adventofcode.y2016.p03

import pt.dmb.adventofcode.common.Utilities

class PartTwo {
    private var possibles = 0
    private val lines = mutableListOf<List<Int>>()

    fun addLine(one: Int, two: Int, three: Int) {
        lines.add(listOf(one, two, three))
    }

    fun increaseIfNeeded(one: Int, two: Int, three: Int) {
        if ((one < two + three) && (two < one + three) && (three < one + two)) {
            possibles++
        }
    }

    fun possibles() = possibles

    fun lines(): List<List<List<Int>>> {
        return lines.chunked(3)
    }
}

fun main() {
    val solver = PartTwo()

    Utilities.readInputFile(2016, 3, scope = "main").forEach { line ->
        val splitLine = line.trim().split("\\s+".toRegex())

        val one = splitLine[0].toInt()
        val two = splitLine[1].toInt()
        val three = splitLine[2].toInt()

        solver.addLine(one, two, three)
    }

    solver.lines().forEach { it ->
        for (index in 0..2) {
            val one = it[0][index]
            val two = it[1][index]
            val three = it[2][index]

            solver.increaseIfNeeded(one, two, three)
        }
    }

    println(solver.possibles())
}
