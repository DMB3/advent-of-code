import common

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        cpu = common.VideoCPU()

        for line in common.read_file(input_file):
            if line == "noop":
                cpu.no_op()
            else:
                instruction, arguments = line.split(" ")
                if instruction == "addx":
                    cpu.add("x", int(arguments))

        for line in cpu.screen:
            print(line)
