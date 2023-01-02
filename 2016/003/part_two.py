import common

if __name__ == "__main__":
    for input_file in common.inputs:
        possibles = 0
        lines = []

        for line in common.read_file(input_file):
            one, two, three = line.split()
            lines.append([int(one), int(two), int(three)])

        for line_one, line_two, line_three in zip(*[iter(lines)] * 3):
            for index in range(3):
                one, two, three = int(line_one[index]), int(line_two[index]), int(line_three[index])
                if int(one) < int(two) + int(three) and \
                        int(two) < int(one) + int(three) and \
                        int(three) < int(one) + int(two):
                    possibles += 1

        print(possibles)
