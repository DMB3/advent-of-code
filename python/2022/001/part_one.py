import common

if __name__ == "__main__":
    for input_file in common.inputs:
        elf_calories = []
        most_calories = 0

        for line in common.read_file(input_file):
            if line == "":
                most_calories = max(most_calories, sum(elf_calories))
                elf_calories = []
            else:
                elf_calories.append(int(line))

        # to make sure the last elf is taken into account
        most_calories = max(most_calories, sum(elf_calories))

        print(most_calories)
