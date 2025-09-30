from src.classes import *
from src.functions import *

# 1º: generar la deck (funcion load_deck) 
deck = load_deck()

# 2º: cargar mano y asignarle cartas 
hand = Hand()
for i in range(0,7):
    hand.add_card(deck)

hand.show_hand()

#3º: pasarle el analizador a la mano
potencial_mano = analyze(hand)



