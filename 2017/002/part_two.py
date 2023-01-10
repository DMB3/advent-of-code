import common

if __name__ == "__main__":
    for input_file in common.inputs:
        result = 0

        for line in common.read_file(input_file):
            numbers = [int(x) for x in line.replace("\t", " ").split(" ")]
            for i in range(len(numbers) - 1):
                for j in range(i + 1, len(numbers)):
                    one, two = numbers[i], numbers[j]
                    if one % two == 0:
                        result += one / two
                    elif two % one == 0:
                        result += two / one

        print(int(result))
