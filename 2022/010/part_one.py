import common

if __name__ == "__main__":
    for input_file in common.inputs:
        cpu = common.VideoCPU()

        for line in common.read_file(input_file):
            if line == "noop":
                cpu.no_op()
            else:
                instruction, arguments = line.split(" ")
                if instruction == "addx":
                    cpu.add("x", int(arguments))

        result = 0
        for cycle in cpu.relevant_strenghts:
            result += cpu.relevant_strenghts[cycle]["x"]
        print(result, cpu.relevant_strenghts)
