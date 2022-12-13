import common
import math

if __name__ == "__main__":
    for input_file in common.inputs:
        result = 0

        for line in common.read_file(input_file):
            mass = int(line)
            fuel = math.floor(mass / 3) - 2
            result += fuel

        print(result)
