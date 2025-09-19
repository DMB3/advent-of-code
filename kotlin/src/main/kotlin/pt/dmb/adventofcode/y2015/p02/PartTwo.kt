package pt.dmb.adventofcode.y2015.p02

import pt.dmb.adventofcode.common.Utilities

class PartTwo(
    private val length: Int,
    private val width: Int,
    private val height: Int,
) {
    fun volume() = length * width * height
    fun minPerimeter() = listOf(2 * width + 2 * length, 2 * width + 2 * height, 2 * length + 2 * height).min()
}

fun main() {
    var result = 0

    Utilities.readInputFile(2015, 2, scope = "main").forEach { line ->
        val splits = line.split("x")

        val length = splits[0].toInt()
        val width = splits[1].toInt()
        val height = splits[2].toInt()

        val solver = PartTwo(length, width, height)

        result += solver.volume() + solver.minPerimeter()
    }

    println(result)
}
