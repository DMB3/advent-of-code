import common

if __name__ == "__main__":
    for input_file in common.inputs:
        instructions = []
        for line in common.read_file(input_file):
            instructions += [int(n) for n in line.split(",")]

        if input_file == "inputs/real_input.txt":
            instructions[1] = 12
            instructions[2] = 2

        start_index = 0
        while len(instructions) > 0:
            opcode, first, second, result = instructions[start_index:start_index+4]
            start_index += 4

            if opcode == 99:
                print("End!")
                break

            first_value = instructions[first]
            second_value = instructions[second]
            if opcode == 1:
                print("Adding", first_value, "with", second_value, "at indexes", first, "and", second)
                print("Storing it at index", result)
                instructions[result] = first_value + second_value
                print("\t", instructions)
            elif opcode == 2:
                print("Multiplying", first_value, "with", second_value, "at indexes", first, "and", second)
                print("Storing it at index", result)
                instructions[result] = first_value * second_value
                print("\t", instructions)
            else:
                print("Unknown opcode", opcode)
                raise ValueError()

        print(input_file, instructions[0])
