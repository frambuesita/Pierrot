import json

##################################################
############## CODIGO SECRETO ####################
##################################################
# 0 : LA MANO ES DE LO QUE SEA
# 6 : LA MANO ES IMPOSIBLE QUE SEA DE LO Q SEA

# Funcion para recorrer el deck.json de la carpeta database
def load_deck():
    """Carga todas las cartas de deck.json y las devuelve como una lista de diccionarios."""
    with open('database/deck.json', "r") as f:
        deck = json.load(f)
    return [card for card in deck.values()]

def analyze(hand):
    return isRoyalFlush(hand.cards_list)

def isRoyalFlush(card_list):
    #comprobar si el palo es el mismo en todas
    return_value = 0
    first_suit = card_list[0].suit
    for card in card_list:
        if card.suit != first_suit:
            return_value = 6 # si no son del mismo palo no puede salir Royal Flush (en realidad si puede, pero no nos conviene valorar la posibilidad)
        else:
            # comprobar si los valores de los simbolos, ordenados, son [10, 11, 12, 13, 14]
            card_values = []
            desired_values = [10,11,12,13,14]
            for card in card_list:
                card_values.append(card.value)

            return_value = set(desired_values) - set(card_values) #cuenta cuantos elementos de la lista de desired_values no estan en card_values
    
    return return_value


    
    
    

