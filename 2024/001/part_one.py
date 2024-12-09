import common

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        left_numbers, right_numbers = [], []
        for line in common.read_file(input_file):
            parts = line.split(" ")
            left_numbers.append(int(parts[0]))
            right_numbers.append(int(parts[-1]))

        left_numbers.sort()
        right_numbers.sort()

        result = 0
        for idx in range(len(left_numbers)):
            left, right = left_numbers[idx], right_numbers[idx]
            result += abs(left - right)

        print(result)
