from typing import Dict, List

import common


def parse_stack(line: str) -> Dict[int, List[str]]:
    result = {}
    current_stack = 1

    while len(line) > 0:
        part = line[:4].strip()

        line = line[4:]
        if len(part) > 0:
            part = part[1:][:1]
            if part:
                result[current_stack] = [part]

        current_stack += 1

    return result


def move_crates(stacks: Dict[int, List[str]], how_many: int, source: int, target: int) -> Dict[int, List[str]]:
    for _ in range(how_many):
        item = stacks[source].pop(0)
        stacks[target].insert(0, item)

    return stacks


if __name__ == "__main__":
    for input_file in common.inputs:
        stacks = {}
        instructions = False

        for line in common.read_file(input_file, strip_lines=False):
            if line.strip() == "":
                instructions = True
                continue

            if instructions:
                move, how_many, from_, source, to, target = line.split(" ")
                how_many, source, target = int(how_many), int(source), int(target)
                stacks = move_crates(stacks, how_many, source, target)
            else:
                parsed = parse_stack(line)

                for stack in parsed:
                    if stack not in stacks:
                        stacks[stack] = []

                    stacks[stack] += parsed[stack]

        result = ""
        for index in sorted(stacks.keys()):
            result += stacks[index][0]

        print(result)
