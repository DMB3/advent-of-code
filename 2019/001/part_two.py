import common
import math


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2


if __name__ == "__main__":
    for input_file in common.inputs:
        result = 0

        for line in common.read_file(input_file):
            mass = int(line)

            for_mass = calculate_fuel(mass)
            # print("mass", mass, "requires", result)

            fuel = calculate_fuel(for_mass)
            # print("fuel of fuel is", fuel)
            while fuel > 0:
                for_mass += fuel
                # print("kept on calculating at", fuel)
                fuel = calculate_fuel(fuel)

            result += for_mass

        print(result)
