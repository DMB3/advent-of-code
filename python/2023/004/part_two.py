import common

if __name__ == "__main__":
    for input_file in common.inputs:
        cards = {}
        for line in common.read_file(input_file):
            card, numbers = [x.strip() for x in line.split(":")]
            card_number = int(card[len("Card "):])
            winners, held = [x.strip() for x in numbers.split("|")]

            winning_numbers = [int(x) for x in winners.split(" ") if len(x) > 0]
            held_numbers = [int(x) for x in held.split(" ") if len(x) > 0]

            common_numbers = list(set(held_numbers).intersection(winning_numbers))

            cards[card_number] = {
                "common_numbers": len(common_numbers),
                "copies": 1
            }

        for i in range(1, len(cards) + 1):
            for time in range(cards[i]["copies"]):
                for copy_number in range(1, cards[i]["common_numbers"] + 1):
                    cards[i + copy_number]["copies"] += 1

        result = 0
        for card in cards:
            result += cards[card]["copies"]

        print(input_file, result)
