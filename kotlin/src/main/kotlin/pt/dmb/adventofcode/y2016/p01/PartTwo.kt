package pt.dmb.adventofcode.y2016.p01

import pt.dmb.adventofcode.common.SantaBetterSleigh
import pt.dmb.adventofcode.common.Utilities
import kotlin.math.absoluteValue

class PartTwo {
    val sleigh = SantaBetterSleigh()

    fun distance() = sleigh.location().first.absoluteValue + sleigh.location().second.absoluteValue
}

fun main() {
    Utilities.readInputFile(2016, 1, scope = "main").forEach { line ->
        val solver = PartTwo()

        line.split(",").forEach { instruction ->
            val direction = instruction.trim()[0]
            val amount = instruction.trim().substring(1).toInt()

            solver.sleigh.turn(direction)
            solver.sleigh.walk(amount)
            if (solver.sleigh.shouldStop()) {
                println("Repeated at ${solver.sleigh.location()} which is ${solver.distance()} steps away")
                return
            }

            solver.sleigh.addSeenLocation(solver.sleigh.location())
        }

        println("Ended at ${solver.sleigh.location()} which is ${solver.distance()} away")
    }
}
