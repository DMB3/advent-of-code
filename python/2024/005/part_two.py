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


def put_in_right_order(rules, update):
    ordered_update = update.copy()
    while True:
        for rule in rules:
            try:
                before_index = ordered_update.index(rule[0])
                after_index = ordered_update.index(rule[1])
                if before_index > after_index:
                    ordered_update[before_index], ordered_update[after_index] = ordered_update[after_index], \
                                                                                ordered_update[before_index]
            except ValueError:
                continue

        if in_right_order(rules, ordered_update):
            break

    return ordered_update


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
            if not in_right_order(rules, update):
                ordered_update = put_in_right_order(rules, update)
                result += middle_element(ordered_update)

        print(result)
