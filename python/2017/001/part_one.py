import common

if __name__ == "__main__":
    for input_file in common.inputs:
        for line in common.read_file(input_file):
            result = 0

            for n in range(len(line)):
                one, two = line[n], line[(n+1) % len(line)]

                if one == two:
                    result += int(one)

            print(result)

