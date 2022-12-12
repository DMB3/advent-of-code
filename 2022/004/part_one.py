import common

if __name__ == "__main__":
    for input_file in common.inputs:
        pairs = 0

        for line in common.read_file(input_file):
            elf_one, elf_two = line.split(",")

            one_start, one_end = elf_one.split("-")
            two_start, two_end = elf_two.split("-")

            set_one = set(range(int(one_start), int(one_end)+1))
            set_two = set(range(int(two_start), int(two_end)+1))
            intersection = set_one.intersection(set_two)

            if len(intersection) == len(set_one) or len(intersection) == len(set_two):
                pairs += 1

        print(pairs)
