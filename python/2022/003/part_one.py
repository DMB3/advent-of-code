import common
from math import floor

if __name__ == "__main__":
    for input_file in common.inputs:
        result = 0

        for line in common.read_file(input_file):
            middle = floor(len(line) / 2.0)
            first, second = line[:middle], line[middle:]
            common_characters = list(set(first).intersection(set(second)))
            for character in common_characters:
                if character.islower():
                    result += ord(character) - 96
                else:
                    result += ord(character) - 38

        print(result)

