# ***************************************************************************************
# Significados especiales de la devolución de las funciones de comprobación
# 0 : LA MANO ES DE LO QUE SEA
# 6 : YA NO SE PUEDE ALCANZAR LA MANO CON LAS CARTAS ACTUALES
# ***************************************************************************************

import json
from collections import Counter


# Funcion para cargar todas las cartas de deck.json y las devolverlas como una lista de diccionarios.
def load_deck():
    with open('database/deck.json', "r") as f:
        deck = json.load(f)
    return [card for card in deck.values()]


def analyze(hand):
    #calcular, dado una mano de cartas, la probabilidad de cada tipo de mano
    royalflush_prob = (1 / isRoyalFlush(hand) * 52) if isRoyalFlush(hand) != 6 else 0
    straightflush_prob = (1 / isStraightFlush(hand) * 13) if isStraightFlush(hand) != 6 else 0 #Aun tengo que pensar en la probabilidad de que salga carta que cumpla la condicion de straight flush
    fourofakind_prob = (1 / isFourofaKind(hand) * 13) if isFourofaKind(hand) != 6 else 0
    fullhouse_prob = (1 / isFullHouse(hand) * 13) if isFullHouse(hand) != 6 else 0
    flush_prob = (1 / isFlush(hand) * 4) if isFlush(hand) != 6 else 0
    straight_prob = (1 / isStraight(hand) * 10) if isStraight(hand) != 6 else 0
    threeofakind_prob = (1 / isThreeofaKind(hand) * 13) if isThreeofaKind(hand) != 6 else 0
    twopair_prob = (1 / isTwoPairs(hand) * 13) if isTwoPairs(hand) != 6 else 0
    par_prob = (1 / isPar(hand) * 13) if isPar(hand) != 6 else 0
    highcard_prob = 1

    #insertar en variables el valor de cada mano completa (asignado a criterio personal)
    royalflush_value = 100
    straightflush_value = 100
    fourofakind_value = 90
    fullhouse_value = 80
    flush_value = 60
    straight_value = 50
    threeofakind_value = 40
    twopair_value = 30
    par_value = 20
    highcard_value = 0
    
    total_value = (royalflush_value * royalflush_prob + straightflush_value * straightflush_prob + fourofakind_value * fourofakind_prob + fullhouse_value * fullhouse_prob +
                   flush_value * flush_prob + straight_value * straight_prob + threeofakind_value * threeofakind_prob + twopair_value * twopair_prob + par_value * par_prob + highcard_value * highcard_prob) / 9

    return total_value

def isRoyalFlush(card_list):
    return_value = 0

    # Tomamos las cartas que tengan value > 10 (es decir, que sean un [10, 'jack', 'queen', 'king' o 'ace'])
    mapped_cards = [i for i in card_list if i.value >= 10]

    cards_suit = [card.suit for card in mapped_cards]
    counter = Counter(cards_suit)
    mode = max(counter, key=counter.get) #El palo más repetido

    remaining_card_values = [10, 11, 12, 13, 14]
    cards_values = [card.value for card in mapped_cards if card.suit == mode]
    remaining_card_values = set(remaining_card_values) - set(cards_values)

    # Si me faltan tantas cartas que en las que me faltan para 7 no podría conseguir la mano
    if len(card_list) + len(remaining_card_values) > 7: 
        return_value = 6 
    else:
        return_value = len(remaining_card_values) # Número de cartas para tener Royal Flush
    return return_value


def isStraightFlush(card_list):
    return_value = 0
    min_missing_values = 4

    cards_suit = [card.suit for card in card_list]
    counter = Counter(cards_suit)
    mode = max(counter, key=counter.get) #El palo más repetido
    cards_values = [card.value for card in card_list if card.suit == mode]
    #Ordenación y eliminación de duplicados
    cards_values = sorted(cards_values)
    
    # Para cada valor, veremos cuantos de los siguientes valores están en la mano y escogeremos el que más cerca esté de escalera
    # e.j: Tenemos un as (1), por lo que se comprueban [2, 3, 4, 5] para ver cuales están en la mano y determinar cuanto queda para
    # hacer una escalera desde 1
    for value in cards_values:
        missing_cards = 4 
        for next_value in range(value + 1, value + 5):
            print(next_value)
            if next_value in cards_values:
                missing_cards -= 1
                print("MISSINGS")
                print(missing_cards)
        min_missing_values = min(missing_cards, min_missing_values)
    
    return_value = min_missing_values # Para estandarizar nomenclatura
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

# DEBEMOS RECORRER EN SENTIDO CONTRARIO ESTO, TODO
    for i in range(len(repeticiones)):
        if repeticiones[i] >= 3: # Si ya tenemos el trio veremos si atras tenemos un par
            if repeticiones[i - 1] >= 2: #Si tambien tenemos par tenemos un full house, asi que el return_value sera 1 
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

def isStraight(card_list):
    card_values = []
    for card in card_list:
        card_values.append(card.value)
        
    contador = 5
    card_values.sort()
    for i in range(len(card_values)-1): #Idea: despues de ordenar, si el valor siguiente - el actual da 1, no hace nada, si no se le resta 1 al contador. El ultimo no se hace
        if card_values[i+1] - card_values[i] == 1:
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

# HACER EL TWO PAIR COMO HICIMOS EL FULL HOUSE TODO (este esta hecho como la mierda)
def isTwoPairs(card_list):
    return_value = 0
    card_values = []
    for card in card_list:
        card_values.append(card.value)

    contador = Counter(card_values)
    repetidos = max(contador.values())

    repetidos_pares = 0
    for count in contador.values():
        if count >= 2:
            repetidos_pares += 1
    if repetidos_pares == 2:
        return_value = 0
    elif repetidos_pares == 1:
        return_value = 1
    elif len(card_values) - (repetidos_pares * 2) > 3:
      return_value = 6
    else:
        return_value = 3
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

def prueba(a, b):
    return a + b
 
            
    
    
    

