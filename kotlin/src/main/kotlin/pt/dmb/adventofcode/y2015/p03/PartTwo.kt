package pt.dmb.adventofcode.y2015.p03

import pt.dmb.adventofcode.common.Utilities

class PartTwo {
    private var santaPosition = Pair(0, 0)
    private var robotPosition = Pair(0, 0)

    private var seen = mutableSetOf(santaPosition)
    private var santasTurn = true

    private fun updatePosition(xIncrement: Int, yIncrement: Int) {
        if (santasTurn) {
            santaPosition = Pair(santaPosition.first + xIncrement, santaPosition.second + yIncrement)
        } else {
            robotPosition = Pair(robotPosition.first + xIncrement, robotPosition.second + yIncrement)
        }
    }

    fun parseInstruction(instruction: Char) {
        when (instruction) {
            '^' -> updatePosition(0, 1)
            'v' -> updatePosition(0, -1)
            '<' -> updatePosition(-1, 0)
            '>' -> updatePosition(1, 0)
        }

        seen.add(santaPosition)
        seen.add(robotPosition)
        swapTurn()
    }

    private fun swapTurn() {
        santasTurn = !santasTurn
    }

    fun seenLength() = seen.size
}

fun main() {
    Utilities.readInputFile(2015, 3, scope = "main").forEach { line ->
        val solver = PartTwo()

        line.toCharArray().forEach { char ->
            solver.parseInstruction(char)
        }

        println(solver.seenLength())
    }
}
