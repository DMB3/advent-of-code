import os

CODE_TEMPLATE = """import common

if __name__ == "__main__":
    for input_file in common.inputs:
        for line in common.read_file(input_file):
            pass
"""

if __name__ == "__main__":
    year = str(int(input("What year should this be for?")))
    day = int(input("What day is this?"))

    if not os.path.exists(year):
        os.mkdir(year)

    puzzle_dir = os.path.join(year, "%03d" % day)
    if not os.path.exists(puzzle_dir):
        os.mkdir(puzzle_dir)

    puzzle_title = input("What is the puzzle title?")

    readme_file = os.path.join(year, "readme.md")
    with open(readme_file, "a") as fout:
        fout.write("- Day %d: [%s](./%03d/)\n" % (day, puzzle_title, day))

    readme_file = os.path.join(puzzle_dir, "readme.md")
    with open(readme_file, "w") as fout:
        fout.write("%s\n" % (puzzle_title,))
        fout.write("%s\n\n" % (len(puzzle_title) * "=",))
        link = "https://adventofcode.com/%s/day/%d" % (year, day,)
        fout.write("%s\n\nBasically a brute force solution...\n" % (link,))

    inputs_directory = os.path.join(puzzle_dir, "inputs")
    os.mkdir(inputs_directory)

    for input_file in ["example_input.txt", "real_input.txt"]:
        with open(os.path.join(inputs_directory, input_file), "w") as fout:
            fout.write("")

    for part_file in ["part_one.py", "part_two.py"]:
        with open(os.path.join(puzzle_dir, part_file), "w") as fout:
            fout.write(CODE_TEMPLATE)
