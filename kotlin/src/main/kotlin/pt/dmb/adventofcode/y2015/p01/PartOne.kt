package pt.dmb.adventofcode.y2015.p01

import pt.dmb.adventofcode.common.Utilities

class PartOne {
    private var floor = 0

    fun parseInstruction(instruction: Char) {
        when (instruction) {
            '(' -> {
                floor += 1
            }

            ')' -> {
                floor -= 1
            }

            else -> {
                throw IllegalArgumentException("Unknown instruction $instruction")
            }
        }
    }

    fun floor(): Int = floor
}

fun main() {
    Utilities.readInputFile(2015, 1, scope = "main").forEach { line ->
        val solver = PartOne()
        line.toCharArray().forEach { char ->
            solver.parseInstruction(char)
        }
        println(solver.floor())
    }
}
