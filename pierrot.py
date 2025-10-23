from src.classes import Card, Hand
from logic.analyzer import analyze, load_deck
from logic.fuzzy import compute_bet

card = Card("Hearts", "Ace", 14)
deck = load_deck()

Pierrot_hand = Hand() 
community_hand = Hand() # Cartas en la mesa que pueden utilizar todos los jugadores

for i in range(0,5):
    community_hand.add_card(deck)

community_cards = community_hand.get_hand()
print(community_cards)

for i in range(0, 2):
    Pierrot_hand.add_card(deck)

print("Mesa:")
community_hand.show_hand()
print("\n\nCartas personales de Pierrot:")
Pierrot_hand.show_hand()


print("\n\nCartas totales de Pierrot (Personales + mesa):")
Pierrot_hand.add_community_cards(community_cards)
Pierrot_hand.show_hand()

#pierrot_potential = analyze(Pierrot_hand.cards_list)
#table_potential = analyze(community_hand)

print(compute_bet(95, 80))


