import common


def is_nice(test):
    found_duplicate_pair = False
    for index in range(0, len(test) - 1):
        one, two = test[index], test[index + 1]
        if one + two in test[index + 2:]:
            found_duplicate_pair = True
            break

    if not found_duplicate_pair:
        return False

    for index in range(0, len(test) - 2):
        one, two = test[index], test[index + 2]
        if one == two:
            return True
        index += 1

    return False


if __name__ == "__main__":
    for input_file in common.inputs:
        nices = 0
        for line in common.read_file(input_file):
            nice = is_nice(line)
            if nice:
                nices += 1

        print(nices)
