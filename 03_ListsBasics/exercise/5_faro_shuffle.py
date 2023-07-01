deck_of_symbols = input().split()
middle_of_deck = len(deck_of_symbols) // 2

first_half_deck = deck_of_symbols[:middle_of_deck]
second_half_deck = deck_of_symbols[middle_of_deck:]

faro_shuffle_times = int(input())

for shuffle in range(faro_shuffle_times):
    shuffled_deck = []
    for cards in range(middle_of_deck):
        shuffled_deck.append(first_half_deck[cards])
        shuffled_deck.append(second_half_deck[cards])
    first_half_deck = shuffled_deck[:middle_of_deck]
    second_half_deck = shuffled_deck[middle_of_deck:]
print(shuffled_deck)