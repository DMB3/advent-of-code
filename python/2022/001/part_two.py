import common

if __name__ == "__main__":
    for input_file in common.inputs:
        all_elves_calories = []
        elf_calories = []

        for line in common.read_file(input_file):
            if line == "":
                all_elves_calories.append(sum(elf_calories))
                elf_calories = []
            else:
                elf_calories.append(int(line))

        # to make sure the last elf is taken into account
        all_elves_calories.append(sum(elf_calories))

        all_elves_calories = sorted(all_elves_calories)[::-1]
        result = 0
        for n in range(3):
            result += all_elves_calories[n]

        print(result)
