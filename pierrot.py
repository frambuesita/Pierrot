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
 █████        █████  ██████  █████     █████      ██████     █████                                                                                                  

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
pb_baraja = ProgressBar(ITERATIONS, text="Generando baraja....")
for i in range(52):
    pb_baraja.update(i)
    sleep(0.01)

pb_reparto = ProgressBar(ITERATIONS, text="Repartiendo cartas....")
for i in range(ITERATIONS):
    pb_reparto.update(i)
    sleep(0.01)

print("\n[CRUPIER] Baraja generada y cartas repartidas.\n")
deck = load_deck()

Pierrot_hand = Hand() 
community_hand = Hand() # Cartas en la mesa que pueden utilizar todos los jugadores

for i in range(0,5):
    community_hand.add_card(deck)

community_cards = community_hand.get_hand()

for i in range(0, 2):
    Pierrot_hand.add_card(deck)

sleep(1)
print("Cartas de la mesa:")
community_hand.show_hand()

sleep(1)
print("\nCartas personales de Pierrot:")
Pierrot_hand.show_hand()

print("\n") 
pb_concatenar = ProgressBar(ITERATIONS, text="Concatenando cartas de Pierrot y la mesa....")
for i in range(ITERATIONS):
    pb_concatenar.update(i)
    sleep(0.001)
print("\n[SISTEMA] Cartas concatenadas.\n")

sleep(1)
print("Cartas totales de Pierrot (Personales + mesa):")
Pierrot_hand.add_community_cards(community_cards)
Pierrot_hand.show_hand()

print("\n")
pb_analisis = ProgressBar(ITERATIONS, text="Analizando potencial de la mano de Pierrot....")
for i in range(ITERATIONS):
    pb_analisis.update(i)
    sleep(0.01)
pb_analisis2 = ProgressBar(ITERATIONS, text="Analizando potencial de la mano comunitaria....")
for i in range(ITERATIONS):
    pb_analisis2.update(i)
    sleep(0.01)

#pierrot_potential = analyze(Pierrot_hand.cards_list)
#table_potential = analyze(community_hand)
pierrot_potential = 95
table_potential = 20
print("\n[SISTEMA] Análisis completo.")
print("Potencial de la mano de Pierrot: ", pierrot_potential, "%.")
print("Potencial de la mano comunitaria: ", table_potential, "%.\n")

pb_logica = ProgressBar(ITERATIONS, text="Calculando apuesta de Pierrot mediante lógica difusa....")
for i in range(ITERATIONS):
    pb_logica.update(i)
    sleep(0.01)

bet = compute_bet(pierrot_potential, table_potential)
print("\n[PIERROT] Pierrot apuesta: ", round(bet, 2), "%.\n")


