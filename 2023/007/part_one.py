import common

if __name__ == "__main__":
    for input_file in common.inputs:
        hands = []

        for line in common.read_file(input_file):
            hand, bid = line.split(" ")

            cards = []
            for card in hand:
                cards.append(common.CamelCard(card))
            hands.append(common.CamelHand(cards, int(bid)))

        result = 0
        for index, hand in enumerate(sorted(hands)):
            result += (index+1) * hand.bid

        print(input_file, result)
