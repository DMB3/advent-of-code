package pt.dmb.adventofcode.y2015.p03

import pt.dmb.adventofcode.common.Utilities

class PartOne {
    private var position = Pair(0, 0)
    private var seen = mutableSetOf(position)

    fun parseInstruction(instruction: Char) {
        position = when (instruction) {
            '^' -> Pair(position.first, position.second + 1)
            'v' -> Pair(position.first, position.second - 1)
            '<' -> Pair(position.first - 1, position.second)
            '>' -> Pair(position.first + 1, position.second)
            else -> position
        }
        seen.add(position)
    }

    fun seenLength() = seen.size
}

fun main() {
    Utilities.readInputFile(2015, 3, scope = "main").forEach { line ->
        val solver = PartOne()

        line.toCharArray().forEach { char ->
            solver.parseInstruction(char)
        }

        println(solver.seenLength())
    }
}
