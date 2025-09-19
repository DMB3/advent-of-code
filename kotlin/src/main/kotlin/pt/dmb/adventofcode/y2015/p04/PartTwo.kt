package pt.dmb.adventofcode.y2015.p04

import pt.dmb.adventofcode.common.Utilities
import java.security.MessageDigest

class PartTwo {
    private var addend = 0
    private val digest = MessageDigest.getInstance("MD5")
    private var solution: String = ""

    @OptIn(ExperimentalStdlibApi::class)
    fun process(line: String): Boolean {
        val md5 = digest.digest("$line$addend".toByteArray()).toHexString()
        if (md5.startsWith("000000")) {
            solution = "$line $addend $md5"
            return true
        }

        addend++
        return false
    }

    fun getSolution() = solution
}

fun main() {
    val solver = PartTwo()
    Utilities.readInputFile(2015, 4, scope = "main").forEach { line ->
        while (true) {
            if (solver.process(line)) {
                return@forEach
            }
        }
    }
    println(solver.getSolution())
}