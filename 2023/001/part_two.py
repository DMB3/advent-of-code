import common

digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

if __name__ == "__main__":
    for input_file in common.inputs:
        result = 0

        for line in common.read_file(input_file):
            found = []
            for i, c in enumerate(line):
                if c.isdigit():
                    found.append(int(c))
                    continue

                for n, digit in enumerate(digit_words):
                    if line[i:].startswith(digit):
                        found.append(n + 1)
                        break
            result += found[0] * 10 + found[-1]

        print(input_file, result)
