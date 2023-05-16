import common

if __name__ == "__main__":
    for input_file in common.inputs:
        if input_file == "inputs/example_input.txt":
            continue

        instructions = []
        for line in common.read_file(input_file):
            instructions += [int(n) for n in line.split(",")]
        original_instructions = instructions.copy()

        all_done = False
        noun, verb = -1, -1

        for noun in range(100):
            if all_done:
                break

            for verb in range(100):
                instructions = original_instructions.copy()
                start_index = 0

                instructions[1] = noun
                instructions[2] = verb

                while len(instructions) > 0:
                    opcode, first, second, result = instructions[start_index:start_index + 4]
                    start_index += 4

                    if opcode == 99:
                        # print("End!")
                        break

                    first_value = instructions[first]
                    second_value = instructions[second]
                    if opcode == 1:
                        # print("Adding", first_value, "with", second_value, "at indexes", first, "and", second)
                        # print("Storing it at index", result)
                        instructions[result] = first_value + second_value
                        # print("\t", instructions)
                    elif opcode == 2:
                        # print("Multiplying", first_value, "with", second_value, "at indexes", first, "and", second)
                        # print("Storing it at index", result)
                        instructions[result] = first_value * second_value
                        # print("\t", instructions)
                    else:
                        print("Unknown opcode", opcode)
                        raise ValueError()

                if instructions[0] == 19690720:
                    all_done = True
                    print(input_file, all_done, instructions[0], noun, verb, 100 * noun + verb)
                    break

