import common

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        for line in common.read_file(input_file):
            floor = 0
            for instruction in line:
                if instruction == "(":
                    floor += 1
                elif instruction == ")":
                    floor -= 1
                else:
                    raise ValueError("Unknown instruction %s" % (instruction,))

            print(floor)
