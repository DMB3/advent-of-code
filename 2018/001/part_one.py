import common

if __name__ == "__main__":
    for input_file in common.inputs:
        frequency = 0

        for line in common.read_file(input_file):
            plus_minus = line[0]
            amount = int(line[1:])

            if plus_minus == "+":
                frequency += amount
            else:
                frequency -= amount

        print(frequency)
