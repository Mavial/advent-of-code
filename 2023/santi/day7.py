from data_loader import DataLoader


def load_data():
    data_loader = DataLoader(day=7, year=2023)
    raw_data = data_loader.load()

    def cards_to_values(cards):
        values = []
        for card in cards:
            match card:
                case "T":
                    values.append(10)
                case "J":
                    values.append(11)
                case "Q":
                    values.append(12)
                case "K":
                    values.append(13)
                case "A":
                    values.append(14)
                case _:
                    values.append(int(card))
        return tuple(values)

    return tuple(map(
        lambda x: (cards_to_values(x[0]), int(x[1])),
        [line.split(" ") for line in raw_data.split("\n")],
    ))


data = load_data()


def part1(): #NOSONAR
    # five of a kind, four of a kind, full house, three of a kind, two pair, one pair, high card
    hand_type = [[], [], [], [], [], [], []]
    for cards, bid in data:
        card_set = set(cards)
        if len(card_set) == 1:
            hand_type[0].append((cards, bid))
        elif len(card_set) == 2:
            if cards.count(cards[0]) == 4 or cards.count(cards[0]) == 1:
                hand_type[1].append((cards, bid))
            else:
                hand_type[2].append((cards, bid))
        elif len(card_set) == 3:
            if (
                cards.count(cards[0]) == 3
                or cards.count(cards[1]) == 3
                or cards.count(cards[2]) == 3
            ):
                hand_type[3].append((cards, bid))
            else:
                hand_type[4].append((cards, bid))
        elif len(card_set) == 4:
            hand_type[5].append((cards, bid))
        else:
            hand_type[6].append((cards, bid))
        for i, t in enumerate(hand_type):
            if len(t) > 1:
                hand_type[i] = sorted(
                    t,
                    reverse=True,
                    key=lambda x: (x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]),
                )
    ranks = sum(hand_type, [])
    ranks_iterator = zip(*ranks)
    next(ranks_iterator)
    ranked_bids = next(ranks_iterator)[::-1]
    result = sum([x * (i + 1) for i, x in enumerate(ranked_bids)])

    return result


def part2(): #NOSONAR
    # five of a kind, four of a kind, full house, three of a kind, two pair, one pair, high card
    p2_data = data[:]
    hand_type = [[], [], [], [], [], [], []]
    for cards, bid in p2_data:
        card_set = set(cards)
        highest_card_by_count = (0, 0)
        for card in card_set:
            count = cards.count(card)
            if count > highest_card_by_count[1] and card != 11:
                highest_card_by_count = (card, count)
        fixed_cards = eval(str(cards).replace("11", "1"))
        cards = eval(str(cards).replace("11", str(highest_card_by_count[0])))
        card_set = set(cards)
        if len(card_set) == 1:
            hand_type[0].append((fixed_cards, bid))
        elif len(card_set) == 2:
            if cards.count(cards[0]) == 4 or cards.count(cards[0]) == 1:
                hand_type[1].append((fixed_cards, bid))
            else:
                hand_type[2].append((fixed_cards, bid))
        elif len(card_set) == 3:
            if (
                cards.count(cards[0]) == 3
                or cards.count(cards[1]) == 3
                or cards.count(cards[2]) == 3
            ):
                hand_type[3].append((fixed_cards, bid))
            else:
                hand_type[4].append((fixed_cards, bid))
        elif len(card_set) == 4:
            hand_type[5].append((fixed_cards, bid))
        else:
            hand_type[6].append((fixed_cards, bid))
        for i, t in enumerate(hand_type):
            if len(t) > 1:
                hand_type[i] = sorted(
                    t,
                    reverse=True,
                    key=lambda x: (x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]),
                )
    ranks = sum(hand_type, [])
    ranks_iterator = zip(*ranks)
    next(ranks_iterator)
    ranked_bids = next(ranks_iterator)[::-1]
    result = sum([x * (i + 1) for i, x in enumerate(ranked_bids)])

    return result

# I had no fun on this one, so the code is respectively horrible.
if __name__ == "__main__":
    print(part1())
    print(part2())
