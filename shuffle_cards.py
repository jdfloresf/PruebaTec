import random

class Card:
    suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

class Deck:
    def __init__(self):
        self.mycardset = []
        for suite in Card.suites:
            for value in Card.values:
                self.mycardset.append(f"{value} of {suite}")

class ShuffleCards:
    def __init__(self, deck):
        self.deck = deck

    def shuffle(self):
        if len(self.deck.mycardset) == 0:
            return "No cards to shuffle"
        random.shuffle(self.deck.mycardset)
        return self.deck.mycardset

    def popCard(self):
        if len(self.deck.mycardset) == 0:
            return "No cards to pop"
        return self.deck.mycardset.pop()

# Uso del código
deck = Deck()
shuffle_deck = ShuffleCards(deck)

print("Deck antes de barajar:")
print(deck.mycardset)

shuffled_cards = shuffle_deck.shuffle()
print("\nDeck después de barajar:")
print(shuffled_cards)

popped_card = shuffle_deck.popCard()
print(f"\nCarta sacada: {popped_card}")

print("\nDeck después de sacar una carta:")
print(deck.mycardset)
