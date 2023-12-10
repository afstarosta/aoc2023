input = open('input.txt', 'r')
lines = input.readlines()

card_values = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

hand_labels = [
    '5',
    '41',
    '32',
    '311',
    '221',
    '2111',
    '11111'
]

labels = {}
for label_index in reversed(hand_labels):
    labels[label_index] = []

def find_hand_label(hand):
    numbers_in_hand = list(set(hand))
    label = []
    for number in numbers_in_hand:
        label.append(str(hand.count(number)))
    return ''.join(sorted(label, reverse=True))

def translate_cards_to_values(hand):
    values = []
    for card in hand:
        values.append(card_values[card])
    return values

hands = []
for line in lines:
    cards, bid = line.split(' ')
    label = find_hand_label(cards)
    hand_info = {
        'cards': cards,
        'bid': int(bid), 
        'label': label,
        'cards_as_values': translate_cards_to_values(cards)
    }
    hands.append(hand_info)
    labels[label].append(hand_info)


sorted_hands = []
for label in labels:
    hands = labels[label]
    sorted_label = sorted(hands, key=lambda element: (element['cards_as_values'][0], element['cards_as_values'][1], element['cards_as_values'][2], element['cards_as_values'][3], element['cards_as_values'][4]))
    sorted_hands += sorted_label

accumulator = 0
for i, hand in enumerate(sorted_hands):
    print("rank: " + str(i + 1) + " hand: " + hand['cards'] + " label: " + hand['label'] + ' values: ' + ','.join(str(x) for x in hand['cards_as_values']))
    accumulator += hand['bid'] * (i + 1)

print(accumulator)