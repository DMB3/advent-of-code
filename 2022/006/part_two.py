import common

TARGET_SIZE = 14

if __name__ == "__main__":
    for input_file in common.inputs:
        for line in common.read_file(input_file):
            so_far = ""

            for character in line:
                while character in so_far:
                    so_far = so_far[1:]

                so_far += character

                if len(so_far) == TARGET_SIZE:
                    break

            print(line, so_far, "\n\t", line.index(so_far) + len(so_far))

