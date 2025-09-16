import common

if __name__ == "__main__":
    ROUND_LIMIT = 10000

    for input_file in common.inputs:
        monkeys = {}

        starting_items = []
        operation = None
        test_predicate = None
        true_case = None
        false_case = None
        monkey_name = None
        divisor = 1
        first = True

        for line in common.read_file(input_file):
            if line.startswith("Monkey"):
                if not first:
                    monkey = common.Monkey(monkey_name, starting_items, operation,
                                           common.MonkeyTest(test_predicate, true_case, false_case))
                    divisor *= monkey.divisor
                    monkeys[monkey.tag] = monkey
                else:
                    monkey_name = int(line.split(" ")[-1][:-1])

                first = False
                monkey_name = int(line.split(" ")[-1][:-1])
                starting_items = []
                operation = None
                test = None
            elif line.startswith("Starting items:"):
                starting_items = [common.MonkeyItem(int(x)) for x in line.split(":")[1].split(",")]
            elif line.startswith("Operation:"):
                operation = line[len("Operation: "):].strip()
            elif line.startswith("Test:"):
                test_predicate = line[len("Test: "):].strip()
            elif line.startswith("If true:"):
                true_case = int(line[len("If true: throw to monkey"):].strip())
            elif line.startswith("If false:"):
                false_case = int(line[len("If false: throw to monkey"):].strip())

        # we have a last monkey to add
        monkey = common.Monkey(monkey_name, starting_items, operation,
                               common.MonkeyTest(test_predicate, true_case, false_case))
        divisor *= monkey.divisor
        monkeys[monkey.tag] = monkey

        # print("Divisor is", divisor)
        current_round = 1
        while current_round <= ROUND_LIMIT:
            # print("Going for round", current_round)
            for monkey_key in sorted(monkeys.keys()):
                monkey = monkeys[monkey_key]

                # print("Monkey %d:" % (monkey.tag,))
                to_remove = []

                for item in monkey.items:
                    # print("\tMonkey inspects an item with a worry level of %d." % (item.value,))
                    monkey.inspection_count += 1

                    monkey.do_operation(item)
                    # print("\t\tAfter operation worry level is %d." % (item.value,))

                    item.mega_boredom(divisor)
                    # print("\t\tAfter boredom worry level is %d" % (item.value,))

                    if monkey.test.perform(item):
                        # print("\t\tCurrent worry level test is true (%s)" % (monkey.test.predicate,))
                        target_monkey = monkey.test.true_case
                    else:
                        # print("\t\tCurrent worry level test is false (%s)" % (monkey.test.predicate,))
                        target_monkey = monkey.test.false_case

                    # print("\t\tItem with worry level %d is thrown to monkey %d" % (item.value, target_monkey))
                    to_remove.append(item)
                    monkeys[target_monkey].items.append(item)
                for item in to_remove:
                    monkey.items.remove(item)

            # print("\tRound ends...")
            # for monkey in monkeys.values():
            # print("\t\t%s" % (monkey,))

            inspections = []
            if current_round == ROUND_LIMIT:
                for monkey in monkeys:
                    # print("Monkey %d inspected items %d times." % (monkey, monkeys[monkey].inspection_count))
                    inspections.append(monkeys[monkey].inspection_count)

                # print(inspections)
                inspections = sorted(inspections)
                print(inspections[-1] * inspections[-2])

            current_round += 1
