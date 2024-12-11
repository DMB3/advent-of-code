import common


def satisfies_rule(update, rule):
    try:
        before_index = update.index(rule[0])
        after_index = update.index(rule[1])
    except ValueError:
        # one or both of them are not in the list at all
        return True

    if before_index != -1 and after_index != -1:
        return before_index < after_index

    return False


def in_right_order(rules, update):
    for rule in rules:
        if not satisfies_rule(update, rule):
            return False

    return True


def middle_element(update):
    middle = len(update) / 2.0
    return update[int(middle - 0.5)]


if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        rules = []
        updates = []
        result = 0

        in_rules = True
        for line in common.read_file(input_file):
            if line.strip() == "":
                in_rules = False
                continue

            if in_rules:
                before, after = [int(x) for x in line.split("|")]
                rules.append((before, after))
            else:
                updates.append([int(x) for x in line.split(",")])

        for update in updates:
            if in_right_order(rules, update):
                result += middle_element(update)

        print(result)
