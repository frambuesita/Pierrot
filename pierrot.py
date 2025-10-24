from src.classes import Card, Hand
from logic.analyzer import analyze, load_deck
from logic.fuzzy import compute_bet
from ezbar import ProgressBar
from time import sleep
# Creamos una portada de Pierrot
title = """   
 ███████████   ███                                         █████        
  ███     ███                                               ███        
  ███     ███ ████   ██████  ████████  ████████   ██████  ███████       
  ██████████   ███  ███  ███  ███  ███  ███  ███ ███  ███   ███         
  ███          ███  ███████   ███       ███      ███  ███   ███        
  ███          ███  ███       ███       ███      ███  ███   ███ ███         
 █████        █████  ██████  █████     █████      ██████     █████                                                                                                    ⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀

    ♠   ♥   ♦   ♣  Sistema de Control de Póker  ♠   ♥   ♦   ♣
 """
print(title)
sleep(2)
#####################################################################

ITERATIONS = 100
pb_pierrot = ProgressBar(ITERATIONS, text="Inicializando Pierrot....")
#Fase 1 de juego: Generación de baraja y reparto de cartas
for i in range(ITERATIONS):
    pb_pierrot.update(i)
    sleep(0.005)

print("\n[SISTEMA] Pierrot inicializado.\n")
pb_baraja = ProgressBar(ITERATIONS, text="Generando baraja")
for i in range(52):
    pb_baraja.update(i)
    sleep(0.05)

pb_reparto = ProgressBar(ITERATIONS, text="Repartiendo cartas")
for i in range(ITERATIONS):
    pb_reparto.update(i)
    sleep(0.05)

print("\nBaraja generada y cartas repartidas.\n")
deck = load_deck()

Pierrot_hand = Hand() 
community_hand = Hand() # Cartas en la mesa que pueden utilizar todos los jugadores

for i in range(0,5):
    community_hand.add_card(deck)

community_cards = community_hand.get_hand()

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
bet = compute_bet(95, 20)
print("[PIERROT] Pierrot apuesta: ", round(bet, 2), "%.\n")


