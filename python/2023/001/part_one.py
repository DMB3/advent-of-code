import common

if __name__ == "__main__":
    for input_file in common.inputs:
        result = 0

        for line in common.read_file(input_file):
            first_digit = None
            for c in line:
                if c.isdigit():
                    first_digit = int(c)
                    break

            second_digit = None
            for c in line[::-1]:
                if c.isdigit():
                    second_digit = int(c)
                    break

            result += (first_digit * 10 + second_digit)

        print(input_file, result)
