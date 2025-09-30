import random

class Card(): 
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
    
    def show_card(self):
        print(str(self.rank) + " of " + self.suit)

class Hand():
    def __init__(self):
        self.cards_list = []
    
    def add_card(self, deck):
        entry = random.choice(deck)
        deck.remove(entry)
        new_card = Card(entry['suit'], entry['rank'], entry['value'])
        self.cards_list.append(new_card)

    def remove_card(self):
        self.cards_list.pop()
    
    def show_hand(self):
        for card in self.cards_list:
            card.show_card()