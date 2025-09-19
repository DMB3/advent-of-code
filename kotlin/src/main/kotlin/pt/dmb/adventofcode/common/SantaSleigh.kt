package pt.dmb.adventofcode.common

open class SantaSleigh {

    protected var facing: FacingDirection = FacingDirection.NORTH
    protected var location: Pair<Int, Int> = Pair(0, 0)

    enum class FacingDirection {
        NORTH, SOUTH, EAST, WEST
    }

    enum class Direction(private val representation: Char) {
        LEFT('L'), RIGHT('R');

        companion object {
            fun fromRepresentation(representation: Char): Direction {
                return entries.first { it.representation == representation }
            }
        }
    }

    fun location() = location

    fun turn(representation: Char) {
        facing = newDirectionOnTurn(Direction.fromRepresentation(representation))
    }

    private fun newDirectionOnTurn(direction: Direction): FacingDirection {
        return when (facing) {
            FacingDirection.NORTH -> if (direction == Direction.RIGHT) FacingDirection.EAST else FacingDirection.WEST
            FacingDirection.SOUTH -> if (direction == Direction.RIGHT) FacingDirection.WEST else FacingDirection.EAST
            FacingDirection.EAST -> if (direction == Direction.RIGHT) FacingDirection.SOUTH else FacingDirection.NORTH
            FacingDirection.WEST -> if (direction == Direction.RIGHT) FacingDirection.NORTH else FacingDirection.SOUTH
        }
    }

    open fun walk(steps: Int) {
        location = newCoordinatesOnWalk(facing, steps)
    }

    private fun newCoordinatesOnWalk(direction: FacingDirection, steps: Int): Pair<Int, Int> {
        return when (direction) {
            FacingDirection.NORTH -> Pair(location.first, location.second - steps)
            FacingDirection.SOUTH -> Pair(location.first, location.second + steps)
            FacingDirection.EAST -> Pair(location.first + steps, location.second)
            FacingDirection.WEST -> Pair(location.first - steps, location.second)
        }
    }
}

class SantaBetterSleigh : SantaSleigh() {
    private val seen = mutableSetOf<Pair<Int, Int>>()
    private var shouldStop: Boolean = false

    init {
        seen.add(location())
    }

    fun shouldStop() = shouldStop

    override fun walk(steps: Int) {
        location = newCoordinatesOnWalk(facing, steps)
    }

    fun addSeenLocation(location: Pair<Int, Int>) {
        seen.add(location)
    }

    private fun newCoordinatesOnWalk(direction: FacingDirection, steps: Int): Pair<Int, Int> {
        return when (direction) {
            FacingDirection.NORTH -> {
                for (i in steps downTo 1) {
                    val newLocation = Pair(location().first, location().second - i)
                    if (seen.contains(newLocation)) {
                        shouldStop = true
                        return newLocation
                    }
                    seen.add(newLocation)
                }

                shouldStop = false
                return Pair(location().first, location().second - steps)
            }

            FacingDirection.SOUTH -> {
                for (i in 1 until steps) {
                    val newLocation = Pair(location().first, location().second + i)
                    if (seen.contains(newLocation)) {
                        shouldStop = true
                        return newLocation
                    }
                    seen.add(newLocation)
                }

                shouldStop = false
                return Pair(location().first, location().second + steps)
            }

            FacingDirection.EAST -> {
                for (i in 1 until steps) {
                    val newLocation = Pair(location().first + i, location().second)
                    if (seen.contains(newLocation)) {
                        shouldStop = true
                        return newLocation
                    }
                    seen.add(newLocation)
                }

                shouldStop = false
                return Pair(location().first + steps, location().second)
            }

            FacingDirection.WEST -> {
                for (i in steps downTo 1) {
                    val newLocation = Pair(location().first - i, location().second)
                    if (seen.contains(newLocation)) {
                        shouldStop = true
                        return newLocation
                    }
                    seen.add(newLocation)
                }

                shouldStop = false
                return Pair(location().first - steps, location().second)
            }
        }
    }
}
