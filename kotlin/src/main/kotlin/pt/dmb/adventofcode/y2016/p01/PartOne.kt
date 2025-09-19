package pt.dmb.adventofcode.y2016.p01

import pt.dmb.adventofcode.common.SantaSleigh
import pt.dmb.adventofcode.common.Utilities
import kotlin.math.absoluteValue

class PartOne {
    val sleigh = SantaSleigh()

    fun distance() = sleigh.location().first.absoluteValue + sleigh.location().second.absoluteValue
}

fun main() {
    Utilities.readInputFile(2016, 1, scope = "main").forEach { line ->
        val solver = PartOne()

        line.split(",").forEach { instruction ->
            val direction = instruction.trim()[0]
            val amount = instruction.trim().substring(1).toInt()

            solver.sleigh.turn(direction)
            solver.sleigh.walk(amount)
        }

        println("Ended at ${solver.sleigh.location()} which is ${solver.distance()} away")
    }
}
