import common


def find_xmas(lines, start_line, start_char, line_inc, char_inc):
    characters_to_find = ["M", "A", "S"]
    current_line, current_char = start_line + line_inc, start_char + char_inc

    while len(characters_to_find) > 0:
        current_character = characters_to_find.pop(0)
        try:
            if current_line < 0 or current_char < 0:
                return False
            if lines[current_line][current_char] != current_character:
                return False
        except IndexError:
            return False

        current_line += line_inc
        current_char += char_inc

    return True


if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        xmas_count = 0

        all_lines = []
        for line in common.read_file(input_file):
            all_lines.append(line)

        for line_number, line in enumerate(all_lines):
            for character_number, character in enumerate(line):
                if character == "X":
                    for line_inc, char_inc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        if find_xmas(all_lines, line_number, character_number, line_inc, char_inc):
                            xmas_count += 1

        print(xmas_count)
