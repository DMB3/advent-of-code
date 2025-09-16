import common

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        left_numbers, right_numbers = [], []
        for line in common.read_file(input_file):
            parts = line.split(" ")
            left_numbers.append(int(parts[0]))
            right_numbers.append(int(parts[-1]))

        result = 0
        for left in left_numbers:
            count = right_numbers.count(left)
            result += (count * left)

        print(result)
