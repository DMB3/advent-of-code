package pt.dmb.adventofcode.y2016.p02

import pt.dmb.adventofcode.common.Utilities

class PartTwo {
    private val keypad = mapOf(
        "1" to mapOf(
            "D" to "3",
        ),
        "2" to mapOf(
            "D" to "6",
            "R" to "3",
        ),
        "3" to mapOf(
            "U" to "1",
            "D" to "7",
            "L" to "2",
            "R" to "4",
        ),
        "4" to mapOf(
            "D" to "8",
            "L" to "3",
        ),
        "5" to mapOf(
            "R" to "6",
        ),
        "6" to mapOf(
            "U" to "2",
            "D" to "A",
            "L" to "5",
            "R" to "7",
        ),
        "7" to mapOf(
            "U" to "3",
            "D" to "B",
            "L" to "6",
            "R" to "8",
        ),
        "8" to mapOf(
            "U" to "4",
            "D" to "C",
            "L" to "7",
            "R" to "9",
        ),
        "9" to mapOf(
            "L" to "8",
        ),
        "A" to mapOf(
            "U" to "6",
            "R" to "B",
        ),
        "B" to mapOf(
            "U" to "7",
            "D" to "D",
            "L" to "A",
            "R" to "C",
        ),
        "C" to mapOf(
            "U" to "8",
            "L" to "B",
        ),
        "D" to mapOf(
            "U" to "B",
        ),
    )
    private var currentKey = "5"
    private var code = ""

    fun readInstruction(instruction: Char) {
        currentKey = keypad[currentKey]!!.getOrDefault(instruction.toString(), currentKey)
    }

    fun updateCode() {
        code += currentKey
    }

    fun code() = code
}

fun main() {
    val solver = PartTwo()

    Utilities.readInputFile(2016, 2, scope = "main").forEach { line ->
        line.forEach { instruction ->
            solver.readInstruction(instruction)
        }

        solver.updateCode()
    }

    println(solver.code())
}