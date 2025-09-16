import common


def find_xmas(lines, start_line, start_char):
    try:
        if start_line - 1 >= 0 and start_char - 1 >= 0:
            if lines[start_line - 1][start_char - 1] == "M" and lines[start_line - 1][start_char + 1] == "S":
                return lines[start_line + 1][start_char - 1] == "M" and lines[start_line + 1][start_char + 1] == "S"
            if lines[start_line - 1][start_char - 1] == "S" and lines[start_line - 1][start_char + 1] == "M":
                return lines[start_line + 1][start_char - 1] == "S" and lines[start_line + 1][start_char + 1] == "M"
            if lines[start_line - 1][start_char - 1] == "M" and lines[start_line - 1][start_char + 1] == "M":
                return lines[start_line + 1][start_char - 1] == "S" and lines[start_line + 1][start_char + 1] == "S"
            if lines[start_line - 1][start_char - 1] == "S" and lines[start_line - 1][start_char + 1] == "S":
                return lines[start_line + 1][start_char - 1] == "M" and lines[start_line + 1][start_char + 1] == "M"
    except IndexError:
        return False

    return False


if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        xmas_count = 0

        all_lines = []
        for line in common.read_file(input_file):
            all_lines.append(line)

        for line_number, line in enumerate(all_lines):
            for character_number, character in enumerate(line):
                if character == "A":
                    if find_xmas(all_lines, line_number, character_number):
                        xmas_count += 1

        print(xmas_count)
