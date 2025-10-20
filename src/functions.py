''' 
Significados especiales de la devolución de las funciones de comprobación
# 0 : LA MANO ES DE LO QUE SEA
# 6 : LA MANO ES IMPOSIBLE QUE SEA DE LO Q SEA
'''

import json
from collections import Counter


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
    if isFlush(card_list) == 6:
        return_value = 6
    else:
        # comprobar si los valores de los simbolos, ordenados, son [10, 11, 12, 13, 14]
        card_values = []
        desired_values = [10,11,12,13,14]
        for card in card_list:
            card_values.append(card.value)

        return_value = set(desired_values) - set(card_values) #cuenta cuantos elementos de la lista de desired_values no estan en card_values
    
    return return_value

def isStraightFlush(card_list):
    return_value = 0
    
    if isFlush(card_list) == 6:
        return_value = 6
    else:
        card_values = []
        for card in card_list:
            card_values.append(card.value)
        
        contador = 5
        card_values.sort()
        for i in range(len(card_values)-1): #Idea: despues de ordenar, si el valor siguiente - el actual da 1, no hace nada, si no se le resta 1 al contador. El ultimo no se hace
            if card_values[i+1] - card_values[i] != 1:
                contador -= 1
        return_value = contador

    return return_value

def isFourofaKind(card_list):
    return_value = 0
    card_values = []
    for card in card_list:
        card_values.append(card.value)

    contador = Counter(card_values)
    repetidos = max(contador.values())

    if len(card_values) - repetidos > 3: #Si la cantidad de cartas dadas que no son el posible póker es mayor de 3, hacer póker es imposible
        return_value = 6
    else:
        return_value = 4 - repetidos

    return return_value

def isFullHouse(card_list):
    return_value = 0
    card_values = []
    for card in card_list:
        card_values.append(card.value)

    contador = Counter(card_values)
    repeticiones = list(contador.values())
    repeticiones.sort()

    for i in range(repeticiones):
        if repeticiones[i] == 3: # Si ya tenemos el trio veremos si atras tenemos un par
            if repeticiones[i - 1] == 2: #Si tambien tenemos par tenemos un full house, asi que el return_value sera 1 
                return_value = 0
            else: #Si no, será 1
                return_value = 1 
        else:
            if repeticiones[i] == 2:
                return_value = 3
            else:
                return_value = 4

    #faltaria meter la situacion que haria imposible hacer un full house, pero no se me termina de ocurrir

    return return_value

def isFlush(card_list):
    return_value = 0
    card_suits = []
    for card in card_list:
        card_suits.append(card.suit)
    
    contador = Counter(card_suits)
    repetidos = max(contador.values())

    if len(card_suits) - repetidos > 2:
        return_value = 6
    else: 
        return_value = 5 - repetidos

    return return_value

def isStraight(card_list):
    card_values = []
    for card in card_list:
        card_values.append(card.value)
        
    contador = 5
    card_values.sort()
    for i in range(len(card_values)-1): #Idea: despues de ordenar, si el valor siguiente - el actual da 1, no hace nada, si no se le resta 1 al contador. El ultimo no se hace
        if card_values[i+1] - card_values[i] != 1:
            contador -= 1
    return_value = contador
    

    return return_value

def isThreeofaKind(card_list):
    return_value = 0
    card_values = []
    for card in card_list:
        card_values.append(card.value)

    contador = Counter(card_values)
    repetidos = max(contador.values())

    if len(card_values) - repetidos > 4:
        return_value = 6
    else:
        return_value = 3 - repetidos
    
    if repetidos == 4: # (hipotesis) Pierrot sobreestimará el valor de la mano si es poker porque tambien será trio y par, asi que en esos casos anulamos la mano anterior
        return_value = 6

    return return_value

def isPar(card_list):
    return_value = 0
    card_values = []
    for card in card_list:
        card_values.append(card.value)

    contador = Counter(card_values)
    repetidos = max(contador.values())

    if len(card_values) - repetidos > 6:
        return_value = 6
    else:
        return_value = 2 - repetidos
    
    if repetidos > 2: 
        return_value = 6

    return return_value

def isHighCard(card_list):
    return 0 #Si la hipotesis es correcta, Pierrot sobreestimará su jugada en algunas ocasiones, pero al valer tan poco carta alta, será inapreciable



 
            


    
    
    

