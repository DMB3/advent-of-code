package pt.dmb.adventofcode.y2015.p01

import pt.dmb.adventofcode.common.Utilities

class PartTwo {
    private var floor = 0
    private var position = 1

    fun parseInstruction(instruction: Char): Boolean {
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

        if (floor == -1) {
            return true
        }

        position += 1
        return false
    }

    fun position(): Int = position
}

fun main() {
    Utilities.readInputFile(2015, 1, scope = "main").forEach { line ->
        val solver = PartTwo()
        line.toCharArray().forEach { char ->
            if (solver.parseInstruction(char)) {
                println(solver.position())
                return
            }
        }
    }
}