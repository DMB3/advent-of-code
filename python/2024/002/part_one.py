import common


def is_safe(the_list):
    differences = [the_list[i + 1] - the_list[i] for i in range(len(the_list) - 1)]
    all_negative = all(difference < 0 and difference in [-3, -2, -1] for difference in differences)
    all_positive = all(difference > 0 and difference in [1, 2, 3] for difference in differences)

    return all_negative or all_positive


if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        safe_reports = 0
        for line in common.read_file(input_file):
            numbers = [int(n.strip()) for n in line.split(" ")]

            if is_safe(numbers):
                safe_reports += 1

        print(safe_reports)
