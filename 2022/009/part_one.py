import common

if __name__ == "__main__":
    for input_file in common.inputs:
        rope = common.Rope()
        # rope.print_status()

        for line in common.read_file(input_file):
            direction, amount = line.split(" ")
            # print(line)
            for _ in range(int(amount)):
                rope.move(direction)
                # rope.print_status()

        print(len(rope.tail_positions))
