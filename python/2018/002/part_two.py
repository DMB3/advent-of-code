import common


def difference_between(one, two):
    if len(one) != len(two):
        return 2e10

    differences = 0
    common_characters = ""
    for index in range(len(one)):
        if one[index] != two[index]:
            differences += 1
        else:
            common_characters += one[index]

    return differences, common_characters


if __name__ == "__main__":
    for input_file in common.inputs:
        lines = []

        for line in common.read_file(input_file):
            lines.append(line)

            if len(lines) == 1:
                continue

            for other in lines:
                if other == line:
                    continue

                difference, common_characters = difference_between(other, line)
                if difference == 1:
                    print("Comparing", other, "with", line, "yields", difference, "with common", common_characters)
