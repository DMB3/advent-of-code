import common

if __name__ == "__main__":
    for input_file in common.inputs:
        two_count = 0
        three_count = 0

        for line in common.read_file(input_file):
            two_counted = False
            three_counted = False

            for letter in line:
                count = line.count(letter)
                if count == 2 and not two_counted:
                    two_count += 1
                    two_counted = True
                elif count == 3 and not three_counted:
                    three_count += 1
                    three_counted = True

        print(two_count, "*", three_count, "=", two_count * three_count)
