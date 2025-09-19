package pt.dmb.adventofcode.common

class SantaSleigh {

    private var facing: FacingDirection = FacingDirection.NORTH
    private var location: Pair<Int, Int> = Pair(0, 0)

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

    fun walk(steps: Int) {
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
