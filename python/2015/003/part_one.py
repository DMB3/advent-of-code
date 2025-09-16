import common

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)

        for line in common.read_file(input_file):
            x, y = (0, 0)
            seen = {(x, y)}
            for instruction in line:
                if instruction == "^":
                    y += 1
                elif instruction == "v":
                    y -= 1
                elif instruction == "<":
                    x -= 1
                elif instruction == ">":
                    x += 1

                seen.add((x, y))

            print(len(seen))
