package pt.dmb.adventofcode.common

import java.io.File

object Utilities {

    fun readInputFile(year: Int, problem: Int, scope: String = "test"): List<String> {
        val path = "src/$scope/resources/$year/${String.format("%02d", problem)}/input.txt"
        return File(path).readLines()
    }
}