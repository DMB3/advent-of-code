package pt.dmb.adventofcode.y2016.p02

import pt.dmb.adventofcode.common.Utilities

class PartOne {
    private val keypad = arrayOf(
        arrayOf(1, 2, 3),
        arrayOf(4, 5, 6),
        arrayOf(7, 8, 9),
    )

    private var rowIndex = 1
    private var columnIndex = 1
    private var code = ""

    fun readInstruction(instruction: Char) {
        when (instruction) {
            'U' -> rowIndex = maxOf(0, rowIndex - 1)
            'D' -> rowIndex = minOf(2, rowIndex + 1)
            'L' -> columnIndex = maxOf(0, columnIndex - 1)
            'R' -> columnIndex = minOf(2, columnIndex + 1)
        }
    }

    fun updateCode() {
        code += keypad[rowIndex][columnIndex].toString()
    }

    fun code() = code
}

fun main() {
    val solver = PartOne()

    Utilities.readInputFile(2016, 2, scope = "main").forEach { line ->
        line.forEach { instruction ->
            solver.readInstruction(instruction)
        }

        solver.updateCode()
    }

    println(solver.code())
}
