import common

if __name__ == "__main__":
    for input_file in common.inputs:
        possibles = 0

        for line in common.read_file(input_file):
            one, two, three = line.split()
            if int(one) < int(two) + int(three) and \
                    int(two) < int(one) + int(three) and \
                    int(three) < int(one) + int(two):
                possibles += 1

        print(possibles)
