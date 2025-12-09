import common

def within_any_range(number, ranges):
    for mini, maxi in ranges:
        if mini <= number <= maxi:
            return True

    return False

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        non_spoiled = 0
        in_ranges = True
        all_ranges = []
        for line in common.read_file(input_file):
            if line.strip() == "":
                in_ranges = False
                continue

            if in_ranges:
                mini, maxi = line.split("-")
                all_ranges.append((int(mini), int(maxi)))
            else:
                ingredient_id = int(line)
                if within_any_range(ingredient_id, all_ranges):
                    non_spoiled += 1

        print(non_spoiled)

