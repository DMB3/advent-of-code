package pt.dmb.adventofcode.y2015.p02

import pt.dmb.adventofcode.common.Utilities

class PartOne(
    private val length: Int,
    private val width: Int,
    private val height: Int,
) {
    fun area() = 2 * length * width + 2 * width * height + 2 * height * length
    fun minSide() = listOf(length * width, width * height, height * length).min()
}

fun main() {
    var result = 0

    Utilities.readInputFile(2015, 2, scope = "main").forEach { line ->
        val splits = line.split("x")

        val length = splits[0].toInt()
        val width = splits[1].toInt()
        val height = splits[2].toInt()

        val solver = PartOne(length, width, height)

        result += solver.area() + solver.minSide()
    }

    println(result)
}
