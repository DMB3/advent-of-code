import common
import re
import os

if __name__ == "__main__":
    for input_file in [os.path.join("inputs", "another_example_input.txt")] + common.inputs:
        print(input_file)
        result = 0

        should_do = True
        for line in common.read_file(input_file):
            found = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line)
            for piece in found:
                first, second, is_do, is_dont = piece[0], piece[1], len(piece[2]) > 0, len(piece[3]) > 0
                if is_do or is_dont:
                    should_do = is_do
                else:
                    if should_do:
                        result += int(first) * int(second)

        print(result)
