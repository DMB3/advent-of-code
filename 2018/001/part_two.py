import common

if __name__ == "__main__":
    for input_file in common.inputs:
        frequency = 0
        found = set()

        operations = []
        for line in common.read_file(input_file):
            plus_minus = line[0]
            amount = int(line[1:])
            operations.append((plus_minus, amount))

        duplicate_found = False
        while not duplicate_found:
            for plus_minus, amount in operations:
                if plus_minus == "+":
                    frequency += amount
                else:
                    frequency -= amount

                if frequency in found:
                    duplicate_found = True
                    break
                found.add(frequency)

        print(frequency)
