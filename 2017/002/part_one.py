import common

if __name__ == "__main__":
    for input_file in common.inputs:
        result = 0

        for line in common.read_file(input_file):
            numbers = [int(x) for x in line.replace("\t", " ").split(" ")]
            result += max(numbers) - min(numbers)

        print(result)
