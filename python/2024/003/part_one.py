import common
import re

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        result = 0

        for line in common.read_file(input_file):
            found = re.findall(r"mul\((\d+),(\d+)\)", line)
            for piece in found:
                first, second = [int(x) for x in piece]
                result += first * second

        print(result)
