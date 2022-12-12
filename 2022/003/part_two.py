import common


def do_group(group):
    result = 0

    common_characters = list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))

    for character in common_characters:
        if character.islower():
            result += ord(character) - 96
        else:
            result += ord(character) - 38

    return result


if __name__ == "__main__":
    for input_file in common.inputs:
        group = []
        result = 0

        for line in common.read_file(input_file):
            group.append(line)
            if len(group) == 3:
                result += do_group(group)
                group = []

        if len(group) == 3:
            result += do_group(group)

        print(result)
