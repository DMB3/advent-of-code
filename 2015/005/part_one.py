import common


def is_nice(test):
    forbidden = ["ab", "cd", "pq", "xy"]
    for nope in forbidden:
        if nope in test:
            return False

    vowels = [char for char in test if char in "aeiouAEIOU"]
    if len(vowels) < 3:
        return False

    has_dupe = False
    for a in range(len(test) - 1):
        if test[a] == test[a + 1]:
            has_dupe = True
            break

    if not has_dupe:
        return False

    return True


if __name__ == "__main__":
    for input_file in common.inputs:
        nices = 0
        for line in common.read_file(input_file):
            if is_nice(line):
                nices += 1

        print(nices)
