import common

if __name__ == "__main__":
    for input_file in common.inputs:
        result = 0

        for line in common.read_file(input_file):
            card, numbers = [x.strip() for x in line.split(":")]
            winners, held = [x.strip() for x in numbers.split("|")]

            winning_numbers = [int(x) for x in winners.split(" ") if len(x) > 0]
            held_numbers = [int(x) for x in held.split(" ") if len(x) > 0]

            common_numbers = list(set(held_numbers).intersection(winning_numbers))
            if len(common_numbers) > 0:
                score = 1
                common_numbers.pop()
                while len(common_numbers) > 0:
                    score *= 2
                    common_numbers.pop()

                result += score

        print(input_file, result)
