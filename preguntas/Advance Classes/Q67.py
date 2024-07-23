#67. Write a Python class to represent a deck of cards and implement 
# methods to shuffle and deal cards.

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt")
        return self.cards.pop()

    def __str__(self):
        return f"Deck of {len(self.cards)} cards"


deck = Deck()
print(deck)
deck.shuffle()
print("Shuffling the deck...")
print("\nDealing 5 cards:")
for _ in range(5):
    card = deck.deal()
    print(card)
print(f"\n{deck}")
